import json
import random
from pathlib import Path

# 📚 Sample categories and items
products = [
    "pen", "pencil", "notebook", "marker", "eraser", "sharpener", "ruler",
    "calculator", "folder", "stapler", "paper", "envelope", "glue", "scissors"
]

# 🗣️ Sample Igbo phrases for question templates
question_templates = [
    "Kedu otu m ga-esi zụta {item}?",
    "Ị nwere {item} n'ụlọ ahịa gị?",
    "Ego ole ka {item} na-eri?",
    "Enwere m ike inweta ọtụtụ {item}?",
    "Gịnị bụ ụtụ maka {item}?",
    "Kedu ụdị {item} i nwere?",
    "Ị nwere {item} nke dị mma?",
    "M chọrọ {item}, ị nwere ya?",
    "M nwere ajụjụ gbasara {item}.",
    "Kedu ka m ga-esi jụọ maka {item}?"
]

# 💬 Sample Igbo response templates
answer_templates = [
    "Ee, anyị nwere {item} dị iche iche.",
    "{item} dị ugbu a na ụlọ ahịa anyị.",
    "Ọnụahịa nke {item} bụ ₦{price}.",
    "Ị nwere ike ịzụta ọtụtụ {item} ma nweta ego mbelata.",
    "Biko kpọtụrụ anyị maka ọnụahịa zuru ezu.",
    "Anyị nwere ụdị {item} ọhụrụ.",
    "Ee, {item} anyị dị mma ma sie ike.",
    "Biko mee nhọrọ gị na ndepụta ngwaahịa anyị.",
    "Enwere m ike inye gị ozi zuru ezu banyere {item}.",
    "Jụọ ajụjụ ọ bụla gbasara {item} — anyị nọ ebe a iji nyere gị aka."
]

# 🔁 Function to generate a dataset entry
def generate_entry():
    item = random.choice(products)
    question = random.choice(question_templates).format(item=item)
    price = random.randint(100, 500)  # Simulated price
    answer = random.choice(answer_templates).format(item=item, price=price)
    return {"question": question, "answer": answer}

# 📦 Generate dataset
def generate_dataset(n=100):
    return [generate_entry() for _ in range(n)]

# 💾 Save dataset to JSON file
def save_dataset(data, path="data/igbo_faq.json"):
    Path("data").mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Dataset saved to {path} ({len(data)} records)")

# 🚀 Main function
if __name__ == "__main__":
    dataset = generate_dataset(10)
    save_dataset(dataset)
