var builder = WebApplication.CreateBuilder(args);

// TOTP microservice for AuthPulse. Exposes POST /api/token and GET /healthz.
builder.Services.AddControllers();
builder.Services.AddOpenApi();

// Allow the Razor front-end (and browser clients) to call the API.
const string CorsPolicy = "authpulse";
builder.Services.AddCors(options =>
    options.AddPolicy(CorsPolicy, policy =>
        policy.AllowAnyOrigin().AllowAnyHeader().AllowAnyMethod()));

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseCors(CorsPolicy);
app.MapControllers();

// Friendly root so hitting the API host doesn't 404.
app.MapGet("/", () => Results.Ok(new
{
    service = "AuthPulse API",
    tagline = "Your 2FA codes, in a heartbeat.",
    endpoints = new[] { "POST /api/token", "GET /healthz" }
}));

app.Run();

// Exposed so integration tests / the WebApplicationFactory can reference the entry point.
public partial class Program { }
