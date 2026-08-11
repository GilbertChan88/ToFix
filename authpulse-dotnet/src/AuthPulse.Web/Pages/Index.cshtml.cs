using System.Text;
using System.Text.Json;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace AuthPulse.Web.Pages;

/// <summary>
/// AuthPulse .NET front-end. The browser posts to the <c>Generate</c> handler,
/// which forwards the request to the AuthPulse Web API (the single source of TOTP
/// truth) using a server-side <see cref="HttpClient"/>. No CORS, no stored secrets.
/// </summary>
[IgnoreAntiforgeryToken] // stateless public generator; no session/auth to protect
public class IndexModel(IHttpClientFactory httpClientFactory) : PageModel
{
    private static readonly JsonSerializerOptions JsonOpts = new(JsonSerializerDefaults.Web);

    public string Brand => "AuthPulse";
    public string Tagline => "Your 2FA codes, in a heartbeat.";
    public string Stack => ".NET 9 · Razor Pages + Web API";

    public void OnGet() { }

    public sealed class GenerateInput
    {
        public string? Secret { get; set; }
        public int Digits { get; set; } = 6;
        public int Period { get; set; } = 30;
        public string Algorithm { get; set; } = "SHA1";
    }

    /// <summary>POST <c>/?handler=Generate</c> — proxies to the Web API and returns its JSON.</summary>
    public async Task<IActionResult> OnPostGenerateAsync([FromBody] GenerateInput input)
    {
        if (string.IsNullOrWhiteSpace(input?.Secret))
            return BadRequest(new { ok = false, error = "Please enter a secret key or otpauth URI." });

        var client = httpClientFactory.CreateClient("AuthPulseApi");
        var payload = new StringContent(
            JsonSerializer.Serialize(input, JsonOpts), Encoding.UTF8, "application/json");

        try
        {
            var response = await client.PostAsync("/api/token", payload);
            var body = await response.Content.ReadAsStringAsync();
            // Pass the API's JSON (and status) straight through to the browser.
            return new ContentResult
            {
                Content = body,
                ContentType = "application/json",
                StatusCode = (int)response.StatusCode
            };
        }
        catch (HttpRequestException)
        {
            return StatusCode(502, new
            {
                ok = false,
                error = "Could not reach the AuthPulse API. Is AuthPulse.Api running?"
            });
        }
    }
}
