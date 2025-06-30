import requests

class Generator:
    def __init__(self, product, type_product, platform, range_audience, description):
        self.product = product
        self.type_product = type_product
        self.platform = platform
        self.range_audience = range_audience
        self.description = description

    def generate_prompt(self):
        return (
            f"Buatkan caption promosi untuk platform {self.platform}.\n"
            f"Nama Produk: {self.product}\n"
            f"Tipe Produk: {self.type_product}\n"
            f"Deskripsi: {self.description}\n"
            f"Target Usia: {self.range_audience[0]}-{self.range_audience[1]} tahun.\n"
            f"Gunakan gaya bahasa yang sesuai dan menarik bagi audiens platform tersebut.\n"
            f"Gunakan Bahasa Indonesia."
        )

class API_Generator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.HEADERS = {
            "Authorization": f"Bearer {self.api_key}",
            "Http-Referer": "http://localhost:8501",
            "Content-Type": "application/json",
            "X-Title": "umkm-promotion-ai-generator"
        }

    def generate_caption(self, prompt):
        PAYLOAD = {
            "model": "anthropic/claude-3-haiku",
            "max_tokens": 256,
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                 headers=self.HEADERS, json=PAYLOAD)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return "❌ Error: " + response.json().get("error", {}).get("message", "Unknown error")


#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
#Aroma yang fresh, fruity, tahan lama, cocok untuk dipakai sehari hari