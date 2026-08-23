import os
import requests
from django.core.mail.backends.base import BaseEmailBackend


class ResendAPIBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        api_key = os.getenv("RESEND_API_KEY", "")
        if not api_key:
            print("[Resend] ERROR: RESEND_API_KEY environment variable is missing!")
            return 0

        sent_count = 0
        url = "https://api.resend.com/emails"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        for message in email_messages:
            payload = {
                "from": "Family Dental Care <onboarding@resend.dev>",
                "to": list(message.to),
                "subject": message.subject,
                "html": message.body if message.content_subtype == "html" else f"<pre>{message.body}</pre>",
            }
            try:
                response = requests.post(url, json=payload, headers=headers, timeout=5)
                print(f"[Resend API] Status: {response.status_code}, Response: {response.text}")
                if response.status_code in [200, 201]:
                    sent_count += 1
            except Exception as e:
                print(f"[Resend API] Exception: {e}")

        return sent_count