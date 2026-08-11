var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

// Typed client pointing at the AuthPulse Web API. Base URL is configurable
// (appsettings: "ApiBaseUrl") and defaults to the API's local dev address.
var apiBaseUrl = builder.Configuration["ApiBaseUrl"] ?? "http://localhost:5043";
builder.Services.AddHttpClient("AuthPulseApi", client =>
{
    client.BaseAddress = new Uri(apiBaseUrl);
    client.Timeout = TimeSpan.FromSeconds(10);
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseStaticFiles();
app.UseRouting();
app.MapRazorPages();

app.Run();
