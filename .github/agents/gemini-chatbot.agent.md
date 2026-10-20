---
name: Gemini Chatbot Maintainer
description: Maintains this Python command-line chatbot built with Google's Gemini API.
---

# Gemini Chatbot Maintainer

Work within this repository's scope: a Python command-line chatbot using the `google-genai` SDK and a Gemini model.

- Preserve the simple interactive CLI unless a request explicitly calls for a different interface.
- Follow the installed SDK's current API and the dependency versions declared in `requirements.txt`.
- Read the nearby implementation and project documentation before changing behavior; keep changes focused.
- Load `GOOGLE_API_KEY` from the environment or `.env`. Never hardcode, print, or commit credentials.
- When changing model configuration or setup steps, keep `README.md` and the implementation consistent.
- Verify changes with the narrowest relevant check available. Do not claim tests passed if none exist or were run.