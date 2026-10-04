# ChatGPT Web Application — Modern Responses API + Legacy Experiments

[![GitHub stars](https://img.shields.io/github/stars/AmirMotefaker/ChatGPT-Web-Application?style=flat&logo=github)](https://github.com/AmirMotefaker/ChatGPT-Web-Application/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/AmirMotefaker/ChatGPT-Web-Application?style=flat&logo=github)](https://github.com/AmirMotefaker/ChatGPT-Web-Application/network/members)
[![Python modernization](https://github.com/AmirMotefaker/ChatGPT-Web-Application/actions/workflows/python-modernization.yml/badge.svg)](https://github.com/AmirMotefaker/ChatGPT-Web-Application/actions/workflows/python-modernization.yml)

A runnable Streamlit chat application using the modern OpenAI Responses API, while preserving the project's original Colab/Kaggle/Gradio notebooks as historical learning material.

## Modern 2026 application

[`ChatGPT_Web_Application.py`](ChatGPT_Web_Application.py) is now the supported application entrypoint.

The app uses:

- the official OpenAI Python SDK
- `client.responses.create(...)`
- `response.output_text`
- `OPENAI_API_KEY` from the environment
- `previous_response_id` for multi-turn conversation state
- Streamlit chat components
- `gpt-5.5` as the default model, overridable with `OPENAI_MODEL` or the sidebar

### Setup

```bash
git clone https://github.com/AmirMotefaker/ChatGPT-Web-Application.git
cd ChatGPT-Web-Application
python -m venv .venv
```

Activate it:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Set the API key locally:

```powershell
$env:OPENAI_API_KEY = "your-key-here"
```

or:

```bash
export OPENAI_API_KEY="your-key-here"
```

Run the app:

```bash
streamlit run ChatGPT_Web_Application.py
```

The sidebar lets you change the model and clear the current conversation. Changing the model resets the stored response chain to avoid mixing conversation state across models.

## Architecture

```text
Streamlit UI
    |
    v
ChatGPT_Web_Application.py
    |
    v
openai_service.py
    |
    v
OpenAI Responses API
```

`openai_service.py` isolates the API call from the UI and makes the Responses API contract testable without making paid network requests.

## Historical notebooks

These files are preserved as an archive of the original project:

| File | Status |
| --- | --- |
| `ChatGPT_Web_Application_colab.ipynb` | Legacy educational notebook |
| `ChatGPT_Web_Application_using_Streamlit_colab.ipynb` | Legacy Streamlit/Colab notebook |
| `ChatGPT_Web_Application_using_Gradio_colab.ipynb` | Legacy Gradio/Colab notebook |
| `chatgpt-web-application-kaggle.ipynb` | Legacy Kaggle notebook |
| `chatgpt-web-application-using-gradio.ipynb` | Legacy Gradio notebook |

> [!IMPORTANT]
> The historical notebooks can contain old model names or deprecated OpenAI API patterns. The root Streamlit application is the modern supported path.

## Validation

```bash
python -m unittest discover -s tests -v
python -m compileall -q .
```

GitHub Actions validates the modernization on Python 3.10 and 3.12 and performs offline unit tests, syntax compilation, secret-pattern scanning, and a guard against legacy API usage in modern entrypoints.

## Security

- Never hard-code an API key.
- Use `OPENAI_API_KEY` in your environment or secret manager.
- `.env` and Streamlit secret files are ignored.
- CI does not make live OpenAI API requests.

## Support the project

If the modern Streamlit example or legacy learning material helps you, consider giving the repository a ⭐.

## Author

**Amir Motefaker** — [GitHub](https://github.com/AmirMotefaker) · [Website](https://amirmotefaker.ir)
