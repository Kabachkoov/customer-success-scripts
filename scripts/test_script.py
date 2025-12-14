# Простой тестовый скрипт для начала
print("=" * 50)
print("🚀 Customer Success Scripts")
print("=" * 50)

# Пример данных клиентов
clients = [
    {"name": "ООО ТехноПрофит", "status": "Активный", "score": 85},
    {"name": "ИП Сидоров", "status": "Рисковый", "score": 45},
    {"name": "ГК СтройГрад", "status": "Стабильный", "score": 72}
]

# Вывод информации
print("\n📊 Анализ клиентов:")
print("-" * 30)

for client in clients:
    if client["score"] >= 80:
        emoji = "💚"
    elif client["score"] >= 60:
        emoji = "💛"
    else:
        emoji = "🔴"
    
    print(f"{emoji} {client['name']}: {client['status']} ({client['score']}/100)")

print("\n" + "=" * 50)
print("✅ Скрипт успешно выполнен!")
print("=" * 50)
