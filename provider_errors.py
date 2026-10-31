def format_provider_error(provider: str, status_code: int) -> str:
    if status_code == 401:
        key_name = "GROQ_API_KEY" if provider == "Groq" else "MISTRAL_API_KEY"
        return (
            f"{provider} rejected its API token (HTTP 401). Check `{key_name}` "
            "in your project .env, then restart the app and try again."
        )

    if status_code == 402:
        return (
            f"{provider} requires available inference credits or billing for this "
            "request (HTTP 402). Check your account's credits, billing status, "
            "and access to the selected model/provider."
        )

    if status_code == 429:
        return (
            f"{provider} rate limit or usage quota was reached (HTTP 429). "
            "Wait and try again, or check your account's usage limits."
        )

    if status_code >= 500:
        return (
            f"{provider} is temporarily unavailable (HTTP {status_code}). "
            "Try again later."
        )

    return (
        f"{provider} rejected the request (HTTP {status_code}). "
        "Check the provider's model and account settings."
    )
