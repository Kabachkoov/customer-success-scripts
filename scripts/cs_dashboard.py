#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║                🚀 CSM DASHBOARD PRO v2.0                      ║
║            Customer Success Manager Dashboard                 ║
╚═══════════════════════════════════════════════════════════════╝
Профессиональная панель управления для менеджера по работе с клиентами.
Визуализация метрик, AI-аналитика, автоматические рекомендации.
"""

import json
import os
import sys
import random
from datetime import datetime, timedelta
from collections import Counter, defaultdict

# Эмуляция цветного вывода в консоли Windows
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
    # Для Windows cmd (обычный)
    @staticmethod
    def init_windows():
        if os.name == 'nt':
            os.system('color')

Colors.init_windows()

class CSMDashboard:
    """Основной класс панели управления CSM."""
    
    def __init__(self):
        self.clients_data = self._load_sample_data()
        self.metrics = self._calculate_metrics()
        self.ai_recommendations = []
        
    def _load_sample_data(self):
        """Загружает тестовые данные клиентов."""
        return [
            {
                "id": 1,
                "name": "ООО 'ТехноПрофит'",
                "tier": "Enterprise",
                "manager": "Иван Иванов",
                "status": "active",
                "health_score": 86,
                "mrr": 150000,
                "churn_risk": 0.05,
                "last_activity": "2025-12-10",
                "nps": 9,
                "onboarding_date": "2025-01-15",
                "tags": ["tech", "high_value", "expansion"]
            },
            {
                "id": 2,
                "name": "ГК 'СтройГрад'",
                "tier": "Business",
                "manager": "Мария Петрова",
                "status": "active",
                "health_score": 72,
                "mrr": 75000,
                "churn_risk": 0.15,
                "last_activity": "2025-12-12",
                "nps": 7,
                "onboarding_date": "2025-03-20",
                "tags": ["construction", "stable"]
            },
            {
                "id": 3,
                "name": "ИП Сидоров А.В.",
                "tier": "Startup",
                "manager": "Иван Иванов",
                "status": "at_risk",
                "health_score": 42,
                "mrr": 25000,
                "churn_risk": 0.65,
                "last_activity": "2025-11-28",
                "nps": 3,
                "onboarding_date": "2025-06-10",
                "tags": ["risk", "needs_attention"]
            },
            {
                "id": 4,
                "name": "ООО 'ВекторПлюс'",
                "tier": "Business",
                "manager": "Алексей Смирнов",
                "status": "active",
                "health_score": 78,
                "mrr": 90000,
                "churn_risk": 0.12,
                "last_activity": "2025-12-14",
                "nps": 8,
                "onboarding_date": "2025-02-05",
                "tags": ["growing", "reliable"]
            },
            {
                "id": 5,
                "name": "ГК 'НефтеХим'",
                "tier": "Enterprise",
                "manager": "Мария Петрова",
                "status": "churned",
                "health_score": 28,
                "mrr": 0,
                "churn_risk": 0.95,
                "last_activity": "2025-10-15",
                "nps": 2,
                "onboarding_date": "2024-11-30",
                "tags": ["churned", "enterprise"]
            },
            {
                "id": 6,
                "name": "ООО 'ЛогистикПро'",
                "tier": "Business",
                "manager": "Иван Иванов",
                "status": "active",
                "health_score": 91,
                "mrr": 120000,
                "churn_risk": 0.03,
                "last_activity": "2025-12-15",
                "nps": 10,
                "onboarding_date": "2025-04-12",
                "tags": ["advocate", "upsell_candidate"]
            }
        ]
    
    def _calculate_metrics(self):
        """Рассчитывает ключевые метрики по портфелю."""
        total_mrr = sum(c["mrr"] for c in self.clients_data if c["status"] != "churned")
        total_clients = len([c for c in self.clients_data if c["status"] != "churned"])
        
        # Распределение по статусам
        status_count = Counter(c["status"] for c in self.clients_data)
        
        # Средний health score
        active_clients = [c for c in self.clients_data if c["status"] == "active"]
        avg_health = sum(c["health_score"] for c in active_clients) / len(active_clients) if active_clients else 0
        
        # Распределение по tier
        tier_distribution = Counter(c["tier"] for c in self.clients_data if c["status"] != "churned")
        
        # Клиенты в риске
        at_risk_clients = [c for c in self.clients_data if c["churn_risk"] > 0.3 and c["status"] == "active"]
        
        return {
            "total_mrr": total_mrr,
            "total_clients": total_clients,
            "avg_health_score": round(avg_health, 1),
            "status_distribution": dict(status_count),
            "tier_distribution": dict(tier_distribution),
            "at_risk_count": len(at_risk_clients),
            "at_risk_mrr": sum(c["mrr"] for c in at_risk_clients),
            "avg_nps": round(sum(c["nps"] for c in active_clients) / len(active_clients), 1) if active_clients else 0
        }
    
    def _generate_ai_recommendations(self):
        """Генерирует AI-рекомендации на основе данных."""
        recommendations = []
        
        # 1. Рисковые клиенты
        high_risk = [c for c in self.clients_data if c["churn_risk"] > 0.5 and c["status"] == "active"]
        if high_risk:
            risk_mrr = sum(c["mrr"] for c in high_risk)
            recommendations.append({
                "priority": "🔴 ВЫСОКИЙ",
                "type": "churn_prevention",
                "title": f"Критические риски оттока",
                "description": f"{len(high_risk)} клиентов под угрозой ухода ({risk_mrr:,} руб. MRR)",
                "action": "Провести экстренные встречи на этой неделе",
                "clients": [c["name"] for c in high_risk[:3]]
            })
        
        # 2. Кандидаты на апсейл
        upsell_candidates = [c for c in self.clients_data 
                           if c["health_score"] > 80 and c["churn_risk"] < 0.2 and c["status"] == "active"]
        if upsell_candidates:
            recommendations.append({
                "priority": "🟢 НИЗКИЙ",
                "type": "revenue_growth",
                "title": f"Возможности для роста",
                "description": f"{len(upsell_candidates)} клиентов готовы к апсейлу",
                "action": "Предложить расширенные тарифы или доп. услуги",
                "clients": [c["name"] for c in upsell_candidates[:3]]
            })
        
        # 3. Просроченная активность
        two_weeks_ago = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")
        inactive = [c for c in self.clients_data 
                   if c["last_activity"] < two_weeks_ago and c["status"] == "active"]
        if inactive:
            recommendations.append({
                "priority": "🟡 СРЕДНИЙ",
                "type": "engagement",
                "title": f"Снижение активности",
                "description": f"{len(inactive)} клиентов не проявляли активность 2+ недели",
                "action": "Отправить персонализированные check-in письма",
                "clients": [c["name"] for c in inactive[:3]]
            })
        
        # 4. NPS улучшение
        low_nps = [c for c in self.clients_data if c["nps"] < 7 and c["status"] == "active"]
        if low_nps:
            recommendations.append({
                "priority": "🟡 СРЕДНИЙ",
                "type": "satisfaction",
                "title": f"Низкая удовлетворенность",
                "description": f"{len(low_nps)} клиентов с NPS < 7",
                "action": "Запросить детальный фидбек и предложить решения",
                "clients": [c["name"] for c in low_nps[:3]]
            })
        
        self.ai_recommendations = recommendations
        return recommendations
    
    def display_header(self):
        """Отображает заголовок в стиле GHunt."""
        print(Colors.BLUE + "╔═══════════════════════════════════════════════════════════════╗" + Colors.RESET)
        print(Colors.BLUE + "║" + Colors.BOLD + "                🚀 CSM DASHBOARD PRO v2.0                      " + Colors.RESET + Colors.BLUE + "║")
        print("║" + Colors.CYAN + "            Customer Success Manager Dashboard                 " + Colors.RESET + Colors.BLUE + "║")
        print("╚═══════════════════════════════════════════════════════════════╝" + Colors.RESET)
        print()
        print(Colors.YELLOW + f"📅 Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}" + Colors.RESET)
        print(Colors.YELLOW + f"👤 Менеджер: Иван Иванов" + Colors.RESET)
        print()
    
    def display_metrics(self):
        """Отображает ключевые метрики."""
        print(Colors.BOLD + "📊 КЛЮЧЕВЫЕ МЕТРИКИ ПОРТФЕЛЯ" + Colors.RESET)
        print(Colors.BLUE + "═" * 55 + Colors.RESET)
        
        # Верхняя строка метрик
        metrics_row1 = [
            f"💰 MRR: {self.metrics['total_mrr']:,} руб.",
            f"👥 Клиенты: {self.metrics['total_clients']}",
            f"❤️ Health: {self.metrics['avg_health_score']}/100",
            f"⭐ NPS: {self.metrics['avg_nps']}/10"
        ]
        
        print("  " + " | ".join(metrics_row1))
        
        # Распределение по статусам
        print()
        print(Colors.BOLD + "📈 РАСПРЕДЕЛЕНИЕ КЛИЕНТОВ" + Colors.RESET)
        print(Colors.BLUE + "─" * 55 + Colors.RESET)
        
        status_colors = {
            "active": Colors.GREEN,
            "at_risk": Colors.YELLOW,
            "churned": Colors.RED
        }
        
        for status, count in self.metrics["status_distribution"].items():
            color = status_colors.get(status, Colors.RESET)
            status_ru = {"active": "Активные", "at_risk": "В риске", "churned": "Ушедшие"}.get(status, status)
            percentage = (count / len(self.clients_data)) * 100
            bar = "█" * int(percentage / 5)
            print(f"  {color}{status_ru}: {count} ({percentage:.1f}%) {bar}" + Colors.RESET)
        
        # Рисковые клиенты
        print()
        if self.metrics["at_risk_count"] > 0:
            print(Colors.RED + f"⚠️  КРИТИЧЕСКИЕ РИСКИ: {self.metrics['at_risk_count']} клиентов под угрозой" + Colors.RESET)
            print(Colors.RED + f"   Потенциальная потеря MRR: {self.metrics['at_risk_mrr']:,} руб." + Colors.RESET)
        else:
            print(Colors.GREEN + "✅ Все клиенты стабильны, критических рисков нет" + Colors.RESET)
    
    def display_clients_table(self):
        """Отображает таблицу клиентов."""
        print()
        print(Colors.BOLD + "👥 ОБЗОР КЛИЕНТОВ" + Colors.RESET)
        print(Colors.BLUE + "═" * 85 + Colors.RESET)
        print(f"{'ID':<3} {'Клиент':<25} {'Тип':<10} {'Health':<8} {'MRR':<12} {'Риск':<8} {'Статус':<12}")
        print(Colors.BLUE + "─" * 85 + Colors.RESET)
        
        for client in self.clients_data:
            # Определяем цвет статуса
            if client["status"] == "active":
                status_color = Colors.GREEN
            elif client["status"] == "at_risk":
                status_color = Colors.YELLOW
            else:
                status_color = Colors.RED
            
            # Определяем цвет health score
            if client["health_score"] >= 80:
                health_color = Colors.GREEN
            elif client["health_score"] >= 60:
                health_color = Colors.YELLOW
            else:
                health_color = Colors.RED
            
            # Определяем цвет риска
            if client["churn_risk"] < 0.2:
                risk_color = Colors.GREEN
            elif client["churn_risk"] < 0.5:
                risk_color = Colors.YELLOW
            else:
                risk_color = Colors.RED
            
            # Форматируем строку
            status_ru = {"active": "Активный", "at_risk": "В риске", "churned": "Ушел"}.get(client["status"], client["status"])
            
            print(f"{client['id']:<3} "
                  f"{client['name']:<25.24} "
                  f"{client['tier']:<10} "
                  f"{health_color}{client['health_score']:<8}" + Colors.RESET +
                  f"{client['mrr']:<12,} "
                  f"{risk_color}{client['churn_risk']:<8.2f}" + Colors.RESET +
                  f"{status_color}{status_ru:<12}" + Colors.RESET)
        
        print(Colors.BLUE + "─" * 85 + Colors.RESET)
    
    def display_ai_recommendations(self):
        """Отображает AI-рекомендации."""
        print()
        print(Colors.BOLD + "🤖 AI РЕКОМЕНДАЦИИ" + Colors.RESET)
        print(Colors.BLUE + "═" * 55 + Colors.RESET)
        
        recommendations = self._generate_ai_recommendations()
        
        if not recommendations:
            print("  🎉 Все отлично! Критических действий не требуется.")
            return
        
        for i, rec in enumerate(recommendations, 1):
            print()
            print(f"  {rec['priority']} {rec['title']}")
            print(f"     📝 {rec['description']}")
            print(f"     🎯 {rec['action']}")
            
            if rec['clients']:
                clients_str = ", ".join(rec['clients'][:3])
                if len(rec['clients']) > 3:
                    clients_str += f" и ещё {len(rec['clients']) - 3}"
                print(f"     👥 Затронутые клиенты: {clients_str}")
    
    def display_quick_actions(self):
        """Отображает быстрые действия."""
        print()
        print(Colors.BOLD + "⚡ БЫСТРЫЕ ДЕЙСТВИЯ" + Colors.RESET)
        print(Colors.BLUE + "═" * 55 + Colors.RESET)
        
        actions = [
            ("📧", "Отправить массовое письмо", "email --mass"),
            ("📊", "Сгенерировать еженедельный отчет", "report --weekly"),
            ("🎯", "Запланировать QBR встречи", "meeting --qbr"),
            ("🚨", "Проверить рисковых клиентов", "check --risk"),
            ("💰", "Найти кандидатов на апсейл", "find --upsell"),
            ("📈", "Обновить метрики NPS", "update --nps")
        ]
        
        for i in range(0, len(actions), 2):
            if i + 1 < len(actions):
                print(f"  {actions[i][0]} {actions[i][1]:<25} {actions[i+1][0]} {actions[i+1][1]}")
            else:
                print(f"  {actions[i][0]} {actions[i][1]}")
    
    def display_interactive_menu(self):
        """Отображает интерактивное меню."""
        print()
        print(Colors.BOLD + "🎮 ИНТЕРАКТИВНОЕ МЕНЮ" + Colors.RESET)
        print(Colors.BLUE + "═" * 55 + Colors.RESET)
        
        menu_options = [
            ("1", "📋 Детальный анализ клиента"),
            ("2", "📧 Сгенерировать письмо"),
            ("3", "📊 Создать отчет"),
            ("4", "📅 Запланировать встречи"),
            ("5", "🔄 Обновить данные"),
            ("6", "💾 Экспорт в CSV"),
            ("7", "⚙️  Настройки"),
            ("8", "❌ Выход")
        ]
        
        for i in range(0, len(menu_options), 2):
            if i + 1 < len(menu_options):
                print(f"  {menu_options[i][0]}. {menu_options[i][1]:<30} {menu_options[i+1][0]}. {menu_options[i+1][1]}")
            else:
                print(f"  {menu_options[i][0]}. {menu_options[i][1]}")
        
        print(Colors.BLUE + "─" * 55 + Colors.RESET)
        
        try:
            choice = input(Colors.CYAN + "\n  Выберите действие (1-8): " + Colors.RESET).strip()
            
            if choice == "1":
                self.client_detail_view()
            elif choice == "2":
                print("\n  📧 Генератор писем запускается...")
                # Здесь можно интегрировать email_generator.py
            elif choice == "8":
                print("\n  👋 До новых встреч!")
                sys.exit(0)
            else:
                print(f"\n  ⚠️  Функция {choice} в разработке...")
                
        except KeyboardInterrupt:
            print("\n\n  👋 Выход из программы.")
            sys.exit(0)
    
    def client_detail_view(self):
        """Детальный просмотр клиента."""
        print()
        print(Colors.BOLD + "👤 ДЕТАЛЬНЫЙ АНАЛИЗ КЛИЕНТА" + Colors.RESET)
        print(Colors.BLUE + "═" * 55 + Colors.RESET)
        
        try:
            client_id = int(input("  Введите ID клиента (1-6): "))
            client = next((c for c in self.clients_data if c["id"] == client_id), None)
            
            if not client:
                print("  ❌ Клиент не найден!")
                return
            
            print()
            print(f"  🏢 {Colors.BOLD}{client['name']}{Colors.RESET}")
            print(f"     Тип: {client['tier']}")
            print(f"     Менеджер: {client['manager']}")
            print(f"     Дата онбординга: {client['onboarding_date']}")
            print()
            
            # Health score bar
            health_bar = "█" * int(client['health_score'] / 5) + "░" * (20 - int(client['health_score'] / 5))
            health_color = Colors.GREEN if client['health_score'] >= 80 else Colors.YELLOW if client['health_score'] >= 60 else Colors.RED
            print(f"  ❤️  Health Score: {health_color}{client['health_score']}/100{Colors.RESET}")
            print(f"     {health_color}{health_bar}{Colors.RESET}")
            
            # Метрики
            print(f"  📊 MRR: {client['mrr']:,} руб.")
            print(f"  ⚠️  Риск оттока: {client['churn_risk']:.1%}")
            print(f"  ⭐ NPS: {client['nps']}/10")
            print(f"  📅 Последняя активность: {client['last_activity']}")
            
            # Теги
            if client['tags']:
                print(f"  🏷️  Теги: {', '.join(client['tags'])}")
            
            print()
            input("  Нажмите Enter для возврата...")
            
        except ValueError:
            print("  ❌ Введите число!")
        except Exception as e:
            print(f"  ❌ Ошибка: {e}")
    
    def run(self):
        """Основной цикл запуска дашборда."""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            self.display_header()
            self.display_metrics()
            self.display_clients_table()
            self.display_ai_recommendations()
            self.display_quick_actions()
            self.display_interactive_menu()


# =================== ЗАПУСК ПРОГРАММЫ ===================
if __name__ == "__main__":
    print(Colors.CYAN + """
    ╔═══════════════════════════════════════════════════════╗
    ║                  ИНИЦИАЛИЗАЦИЯ...                     ║
    ║           CSM Dashboard Pro загружается              ║
    ╚═══════════════════════════════════════════════════════╝
    """ + Colors.RESET)
    
    # Имитация загрузки
    for i in range(5):
        print(f"  Загрузка данных... {'█' * (i+1)}{'░' * (4-i)}", end='\r')
        sys.stdout.flush()
        import time
        time.sleep(0.3)
    
    print("\n" + Colors.GREEN + "  ✅ Дашборд готов к работе!" + Colors.RESET)
    print()
    
    # Запуск дашборда
    dashboard = CSMDashboard()
    
    try:
        dashboard.run()
    except KeyboardInterrupt:
        print("\n\n" + Colors.YELLOW + "👋 Выход из CSM Dashboard Pro. Хорошего дня!" + Colors.RESET)
    except Exception as e:
        print("\n" + Colors.RED + f"❌ Критическая ошибка: {e}" + Colors.RESET)
        print("Пожалуйста, сообщите об ошибке разработчику.")
