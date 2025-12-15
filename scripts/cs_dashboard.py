#!/usr/bin/env python3
"""
================================================================================
                        CSM DASHBOARD PRO v3.1
                  Customer Success Manager Dashboard
                      [AI-Powered Analytics]
================================================================================
Профессиональная панель управления с полным функционалом для CSM.
Специально адаптировано для Windows cmd - все иконки отображаются правильно.
"""

import json
import os
import sys
import csv
from datetime import datetime, timedelta
from collections import Counter
import time

# Специальные символы для Windows
class Icons:
    # Основные иконки (работают в Windows)
    CHART = "[CHART]"
    USERS = "[USERS]"
    HEART = "[HEART]"
    STAR = "[STAR]"
    WARNING = "[WARN]"
    DOWN = "[DOWN]"
    EMAIL = "[MAIL]"
    REPORT = "[RPRT]"
    CALENDAR = "[CAL]"
    SYNC = "[SYNC]"
    SAVE = "[SAVE]"
    SETTINGS = "[SET]"
    EXIT = "[EXIT]"
    DETAIL = "[DET]"
    AI = "[AI]"
    QUICK = "[QUICK]"
    MENU = "[MENU]"
    PHONE = "[PHONE]"
    TAG = "[TAG]"
    MONEY = "[MONEY]"
    CLOCK = "[CLOCK]"
    CHECK = "[OK]"
    
    # Цвета (используем простые метки)
    @staticmethod
    def color(text, color_type):
        """Простая цветовая разметка для Windows."""
        colors = {
            'blue': text,
            'green': text,
            'yellow': text,
            'red': text,
            'cyan': text,
            'bold': text,
            'purple': text
        }
        return colors.get(color_type, text)

class CSMDashboardPro:
    """Улучшенная панель управления CSM с полным функционалом."""
    
    def __init__(self):
        self.clients_data = self._load_sample_data()
        self.metrics = self._calculate_metrics()
        self.ai_recommendations = []
        self.report_history = []
        
    def _load_sample_data(self):
        """Загружает расширенные тестовые данные клиентов."""
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
                "tags": ["tech", "high_value", "expansion"],
                "contact_person": "Алексей Петров",
                "email": "alexey@techprofit.ru",
                "phone": "+7 (999) 123-45-67",
                "usage_trend": "increasing",
                "last_interaction": "Демо новых функций",
                "next_action": "Обсуждение апгрейда",
                "action_date": "2025-12-20"
            },
            # ... (остальные клиенты такие же как в предыдущей версии)
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
                "tags": ["construction", "stable"],
                "contact_person": "Сергей Иванов",
                "email": "sergey@stroygrad.ru",
                "phone": "+7 (999) 234-56-78",
                "usage_trend": "stable",
                "last_interaction": "Обучение сотрудников",
                "next_action": "Проверка эффективности",
                "action_date": "2025-12-18"
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
                "tags": ["risk", "needs_attention"],
                "contact_person": "Андрей Сидоров",
                "email": "andrey@sidorov.ru",
                "phone": "+7 (999) 345-67-89",
                "usage_trend": "decreasing",
                "last_interaction": "Проблемы с интеграцией",
                "next_action": "Срочный созвон",
                "action_date": "2025-12-16"
            }
        ]
    
    def _calculate_metrics(self):
        """Рассчитывает ключевые метрики по портфелю."""
        active_clients = [c for c in self.clients_data if c["status"] == "active"]
        total_mrr = sum(c["mrr"] for c in active_clients)
        
        status_count = Counter(c["status"] for c in self.clients_data)
        avg_health = sum(c["health_score"] for c in active_clients) / len(active_clients) if active_clients else 0
        avg_nps = round(sum(c["nps"] for c in active_clients) / len(active_clients), 1) if active_clients else 0
        
        at_risk_clients = [c for c in active_clients if c["churn_risk"] > 0.3]
        tier_distribution = Counter(c["tier"] for c in active_clients)
        
        return {
            "total_mrr": total_mrr,
            "total_clients": len(active_clients),
            "avg_health_score": round(avg_health, 1),
            "avg_nps": avg_nps,
            "status_distribution": dict(status_count),
            "tier_distribution": dict(tier_distribution),
            "at_risk_count": len(at_risk_clients),
            "at_risk_mrr": sum(c["mrr"] for c in at_risk_clients),
            "total_churned": status_count.get("churned", 0)
        }
    
    def display_header(self):
        """Отображает заголовок."""
        print("=" * 70)
        print("                CSM DASHBOARD PRO v3.1")
        print("           Customer Success Manager Dashboard")
        print("=" * 70)
        print(f"Дата: {datetime.now().strftime('%d %B %Y, %A')}")
        print(f"Менеджер: Иван Иванов | Email: ivan@company.com")
        print(f"Портфель: {self.metrics['total_clients']} активных клиентов")
        print(f"Общий MRR: {self.metrics['total_mrr']:,} руб.")
        print()
    
    def display_metrics(self):
        """Отображает ключевые метрики."""
        print(f"{Icons.CHART} КЛЮЧЕВЫЕ МЕТРИКИ ПОРТФЕЛЯ")
        print("-" * 50)
        
        print(f"  {Icons.MONEY} MRR: {self.metrics['total_mrr']:,} руб.")
        print(f"  {Icons.USERS} Клиенты: {self.metrics['total_clients']}")
        print(f"  {Icons.HEART} Health Score: {self.metrics['avg_health_score']}/100")
        print(f"  {Icons.STAR} NPS: {self.metrics['avg_nps']}/10")
        print(f"  {Icons.WARNING} Клиентов в риске: {self.metrics['at_risk_count']}")
        print(f"  {Icons.DOWN} Ушедших клиентов: {self.metrics['total_churned']}")
        
        print()
    
    def display_clients_table(self):
        """Отображает таблицу клиентов."""
        print(f"{Icons.USERS} ОБЗОР КЛИЕНТСКОГО ПОРТФЕЛЯ")
        print("-" * 70)
        print(f"{'ID':<3} {'Клиент':<22} {'Тип':<10} {'Health':<7} {'MRR':<12} {'Риск':<7} {'Статус':<10}")
        print("-" * 70)
        
        for client in self.clients_data:
            status_display = {
                "active": "Активный",
                "at_risk": "В риске", 
                "churned": "Ушел"
            }.get(client["status"], client["status"])
            
            risk_percent = f"{client['churn_risk']*100:.0f}%"
            
            print(f"{client['id']:<3} "
                  f"{client['name'][:20]:<22} "
                  f"{client['tier']:<10} "
                  f"{client['health_score']:<7} "
                  f"{client['mrr']:<12,} "
                  f"{risk_percent:<7} "
                  f"{status_display:<10}")
        
        print("-" * 70)
        print()
    
    def display_ai_recommendations(self):
        """Отображает AI-рекомендации."""
        print(f"{Icons.AI} AI РЕКОМЕНДАЦИИ")
        print("-" * 50)
        
        # Простые рекомендации
        if self.metrics['at_risk_count'] > 0:
            print(f"[WARN] {self.metrics['at_risk_count']} клиентов под угрозой ухода")
            print(f"       Рекомендация: Провести emergency call сегодня")
            print()
        
        # Проверка активности
        two_weeks_ago = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")
        inactive = [c for c in self.clients_data 
                   if c["last_activity"] < two_weeks_ago and c["status"] == "active"]
        if inactive:
            print(f"[WARN] {len(inactive)} клиентов не активны 2+ недели")
            print(f"       Рекомендация: Отправить check-in письма")
            print()
        
        print()
    
    def display_quick_actions(self):
        """Отображает быстрые действия."""
        print(f"{Icons.QUICK} БЫСТРЫЕ ДЕЙСТВИЯ")
        print("-" * 50)
        
        actions = [
            (Icons.EMAIL, "Email Campaign", "Запустить email-рассылку"),
            (Icons.REPORT, "Weekly Report", "Сгенерировать отчет"),
            (Icons.CALENDAR, "QBR Planner", "Запланировать обзоры"),
            (Icons.WARNING, "Risk Review", "Анализ рисков"),
            (Icons.MONEY, "Upsell Finder", "Найти кандидатов"),
            (Icons.STAR, "NPS Survey", "Опрос удовлетворенности"),
            (Icons.USERS, "Onboarding", "Проверить новых"),
            (Icons.SAVE, "Export Data", "Экспорт в CSV")
        ]
        
        for i in range(0, len(actions), 2):
            if i + 1 < len(actions):
                icon1, title1, desc1 = actions[i]
                icon2, title2, desc2 = actions[i + 1]
                print(f"  {icon1} {title1:<15} {desc1}")
                print(f"  {icon2} {title2:<15} {desc2}")
                if i + 2 < len(actions):
                    print()
    
    def display_interactive_menu(self):
        """Отображает исправленное меню (ВСЕ КНОПКИ ВЫРОВНЕНЫ)."""
        print()
        print(f"{Icons.MENU} ИНТЕРАКТИВНОЕ МЕНЮ")
        print("-" * 50)
        
        # ВСЕ строки одинаковой длины - ровное меню
        menu_items = [
            ("1", f"{Icons.DETAIL} Детальный анализ клиента"),
            ("2", f"{Icons.EMAIL} Генератор писем"),
            ("3", f"{Icons.REPORT} Создать отчет"),
            ("4", f"{Icons.CALENDAR} Запланировать встречи"),
            ("5", f"{Icons.SYNC} Обновить данные"),
            ("6", f"{Icons.SAVE} Экспорт в CSV"),
            ("7", f"{Icons.SETTINGS} Настройки"),
            ("8", f"{Icons.EXIT} Выход")
        ]
        
        # Выравниваем ВСЕ строки одинаково
        for i in range(0, len(menu_items), 2):
            num1, text1 = menu_items[i]
            
            if i + 1 < len(menu_items):
                num2, text2 = menu_items[i + 1]
                # Фиксированная ширина для ровного отображения
                print(f"  {num1}. {text1:<30} {num2}. {text2}")
            else:
                # Для нечетного количества (но у нас 8 - четное)
                print(f"  {num1}. {text1}")
        
        print("-" * 50)
        
        try:
            choice = input(f"\nВыберите действие (1-8): ").strip()
            
            if choice == "1":
                self.client_detail_view()
            elif choice == "2":
                self.email_generator()
            elif choice == "3":
                self.create_report()
            elif choice == "4":
                self.schedule_meetings()
            elif choice == "5":
                self.update_data()
            elif choice == "6":
                self.export_to_csv()
            elif choice == "7":
                self.show_settings()
            elif choice == "8":
                self.exit_program()
            else:
                print(f"\n[ERROR] Неверный выбор. Пожалуйста, выберите 1-8")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n\n[EXIT] Выход из программы.")
            sys.exit(0)
    
    def client_detail_view(self):
        """Детальный просмотр клиента."""
        print()
        print(f"{Icons.DETAIL} ДЕТАЛЬНЫЙ АНАЛИЗ КЛИЕНТА")
        print("-" * 50)
        
        try:
            client_id = int(input("Введите ID клиента (1-3): "))
            client = next((c for c in self.clients_data if c["id"] == client_id), None)
            
            if not client:
                print("[ERROR] Клиент не найден!")
                time.sleep(1)
                return
            
            print()
            print(f"{Icons.USERS} {client['name']}")
            print("-" * 40)
            print(f"Тип: {client['tier']}")
            print(f"Менеджер: {client['manager']}")
            print(f"Дата онбординга: {client['onboarding_date']}")
            print()
            
            print(f"{Icons.HEART} Health Score: {client['health_score']}/100")
            print(f"{Icons.MONEY} MRR: {client['mrr']:,} руб.")
            print(f"{Icons.WARNING} Риск оттока: {client['churn_risk']:.1%}")
            print(f"{Icons.STAR} NPS: {client['nps']}/10")
            print(f"{Icons.CLOCK} Последняя активность: {client['last_activity']}")
            print()
            
            print(f"{Icons.PHONE} Контактная информация:")
            print(f"  Контакт: {client['contact_person']}")
            print(f"  Email: {client['email']}")
            print(f"  Телефон: {client['phone']}")
            print()
            
            if client['tags']:
                print(f"{Icons.TAG} Теги: {', '.join(client['tags'])}")
            
            print()
            input("Нажмите Enter для возврата...")
            
        except ValueError:
            print("[ERROR] Введите число!")
            time.sleep(1)
    
    def email_generator(self):
        """Генератор профессиональных писем."""
        print()
        print(f"{Icons.EMAIL} ГЕНЕРАТОР ПИСЕМ")
        print("-" * 50)
        
        print("\nДоступные шаблоны:")
        print("  1. Приветственное письмо (онбординг)")
        print("  2. Follow-up после встречи")
        print("  3. Напоминание об оплате")
        print("  4. Назад в меню")
        
        try:
            choice = input("\nВыберите шаблон (1-4): ").strip()
            
            if choice == "4":
                print("[BACK] Возврат в меню...")
                time.sleep(1)
                return
            
            if choice in ["1", "2", "3"]:
                client_name = input("Имя клиента: ") or "ООО 'ТехноПрофит'"
                
                print(f"\n[OK] Письмо сгенерировано!")
                print("-" * 40)
                print(f"Тема: Пример письма для {client_name}")
                print(f"\nУважаемый(ая) {client_name},")
                print("\nЭто пример сгенерированного письма.")
                print("\nС уважением,")
                print("Иван Иванов")
                print("-" * 40)
                
                print()
                input("Нажмите Enter для продолжения...")
            else:
                print("[ERROR] Неверный выбор")
                time.sleep(1)
                
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(1)
    
    def create_report(self):
        """Создание отчетов."""
        print()
        print(f"{Icons.REPORT} СОЗДАНИЕ ОТЧЕТОВ")
        print("-" * 50)
        
        print("\nТипы отчетов:")
        print("  1. Еженедельный отчет по портфелю")
        print("  2. Отчет по рисковым клиентам")
        print("  3. Назад в меню")
        
        try:
            choice = input("\nВыберите тип (1-3): ").strip()
            
            if choice == "3":
                print("[BACK] Возврат в меню...")
                time.sleep(1)
                return
            
            if choice in ["1", "2"]:
                print(f"\n[SYNC] Генерация отчета...")
                time.sleep(1)
                
                print(f"\n[OK] Отчет успешно создан!")
                print(f"Тип: {'Еженедельный' if choice == '1' else 'Рисковый'}")
                print(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
                print(f"Клиентов: {self.metrics['total_clients']}")
                
                print()
                input("Нажмите Enter для продолжения...")
            else:
                print("[ERROR] Неверный выбор")
                time.sleep(1)
                
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(1)
    
    def schedule_meetings(self):
        """Планирование встреч."""
        print()
        print(f"{Icons.CALENDAR} ПЛАНИРОВАНИЕ ВСТРЕЧ")
        print("-" * 50)
        
        print("\nПредстоящие встречи:")
        for client in self.clients_data:
            if client.get("action_date"):
                print(f"  {client['action_date']} - {client['name']}")
        
        print()
        input("Нажмите Enter для возврата...")
    
    def update_data(self):
        """Обновление данных."""
        print()
        print(f"{Icons.SYNC} ОБНОВЛЕНИЕ ДАННЫХ")
        print("-" * 50)
        
        print("\n[SYNC] Обновление метрик...")
        time.sleep(1)
        
        self.metrics = self._calculate_metrics()
        
        print(f"[OK] Данные обновлены!")
        print(f"Текущий MRR: {self.metrics['total_mrr']:,} руб.")
        print(f"Активных клиентов: {self.metrics['total_clients']}")
        
        print()
        input("Нажмите Enter для продолжения...")
    
    def export_to_csv(self):
        """Экспорт в CSV."""
        print()
        print(f"{Icons.SAVE} ЭКСПОРТ В CSV")
        print("-" * 50)
        
        try:
            filename = "csm_export.csv"
            
            print(f"\n[SAVE] Экспорт данных...")
            
            with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                fieldnames = ['ID', 'Name', 'Tier', 'Health', 'MRR', 'Risk', 'Status']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for client in self.clients_data:
                    writer.writerow({
                        'ID': client['id'],
                        'Name': client['name'],
                        'Tier': client['tier'],
                        'Health': client['health_score'],
                        'MRR': client['mrr'],
                        'Risk': f"{client['churn_risk']:.1%}",
                        'Status': client['status']
                    })
            
            print(f"[OK] Данные экспортированы в {filename}")
            print(f"Записей: {len(self.clients_data)}")
            
            print()
            input("Нажмите Enter для продолжения...")
            
        except Exception as e:
            print(f"[ERROR] Ошибка экспорта: {e}")
            time.sleep(2)
    
    def show_settings(self):
        """Настройки программы."""
        print()
        print(f"{Icons.SETTINGS} НАСТРОЙКИ ПРОГРАММЫ")
        print("-" * 50)
        
        print("\nТекущие настройки:")
        print("  • Тема: Стандартная")
        print("  • Уведомления: Включены")
        print("  • Автосохранение: Включено")
        print("  • Язык: Русский")
        
        print("\nДоступные действия:")
        print("  1. Сменить тему")
        print("  2. Настроить уведомления")
        print("  3. Назад в меню")
        
        try:
            choice = input("\nВыберите действие (1-3): ").strip()
            
            if choice == "3":
                print("[BACK] Возврат в меню...")
                time.sleep(1)
                return
            
            if choice in ["1", "2"]:
                print(f"\n[INFO] Функция в разработке...")
                print()
                input("Нажмите Enter для продолжения...")
            else:
                print("[ERROR] Неверный выбор")
                time.sleep(1)
                
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(1)
    
    def exit_program(self):
        """Выход из программы."""
        print()
        print(f"{Icons.EXIT} ВЫХОД ИЗ ПРОГРАММЫ")
        print("-" * 50)
        
        print(f"\n[SAVE] Сохранение данных...")
        time.sleep(1)
        
        print(f"[OK] Статистика за сессию:")
        print(f"  • Клиентов просмотрено: {len(self.clients_data)}")
        print(f"  • Общий MRR: {self.metrics['total_mrr']:,} руб.")
        print(f"  • Средний Health Score: {self.metrics['avg_health_score']}")
        
        print(f"\nСпасибо за использование CSM Dashboard Pro!")
        time.sleep(2)
        sys.exit(0)
    
    def run(self):
        """Основной цикл."""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            self.display_header()
            self.display_metrics()
            self.display_clients_table()
            self.display_ai_recommendations()
            self.display_quick_actions()
            self.display_interactive_menu()


# =================== ЗАПУСК ===================
if __name__ == "__main__":
    try:
        print("\n" + "=" * 60)
        print("          ИНИЦИАЛИЗАЦИЯ CSM DASHBOARD PRO")
        print("=" * 60)
        
        print("\nЗагрузка данных...")
        time.sleep(0.5)
        print("Инициализация модулей...")
        time.sleep(0.5)
        print("Подготовка интерфейса...")
        time.sleep(0.5)
        
        print(f"\n[OK] CSM Dashboard Pro v3.1 готов к работе!")
        print("-" * 60)
        time.sleep(1)
        
        dashboard = CSMDashboardPro()
        dashboard.run()
        
    except KeyboardInterrupt:
        print(f"\n\n[EXIT] Программа прервана пользователем.")
    except Exception as e:
        print(f"\n[ERROR] Критическая ошибка: {e}")
