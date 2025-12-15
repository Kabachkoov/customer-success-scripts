#!/usr/bin/env python3
"""
CSM DASHBOARD PRO v3.5
Чистая текстовая версия
"""

import os
import sys
import csv
import time
from datetime import datetime

# ================== УНИКАЛЬНАЯ CSM ASCII КАРТИНКА ==================
def display_logo():
    """Уникальная CSM ASCII картинка в стиле terminal"""
    logo = """
     _____ _____ __  __   ____  _   _ _____ 
    / ____/ ____|  \/  | / __ \| \ | |  __ \\
   | |   | |    | \  / || |  | |  \| | |  | |
   | |   | |    | |\/| || |  | | . ` | |  | |
   | |___| |____| |  | || |__| | |\  | |__| |
    \_____\_____|_|  |_| \____/|_| \_|_____/
    
        CUSTOMER SUCCESS MANAGER DASHBOARD
                  Version 3.5
    """
    print(logo)

class Dashboard:
    def __init__(self):
        if os.name == 'nt':
            os.system('chcp 65001 > nul')
        
        self.clients = [
            {"id": 1, "name": "OOO 'TermoProfit'", "type": "Enterprise", "health": 86, "mrr": 150000, "risk": 5, "status": "Active"},
            {"id": 2, "name": "GK 'StroyGrad'", "type": "Business", "health": 72, "mrr": 75000, "risk": 15, "status": "Active"},
            {"id": 3, "name": "IP Sidorov A.V.", "type": "Startup", "health": 42, "mrr": 25000, "risk": 65, "status": "At Risk"},
            {"id": 4, "name": "OOO 'MediaGroup'", "type": "Business", "health": 88, "mrr": 95000, "risk": 8, "status": "Active"}
        ]
        
        self.metrics = {
            "total_mrr": sum(c["mrr"] for c in self.clients),
            "total_clients": len(self.clients),
            "avg_health": 82.0,
            "at_risk": 1
        }

    def display_header(self):
        """Заголовок с информацией"""
        print("=" * 70)
        print("ДАТА: 15 декабря 2023, Понедельник")
        print("МЕНЕДЖЕР: Иван Иванов | Email: ivan@company.com")
        print(f"ПОРТФЕЛЬ: {self.metrics['total_clients']} активных клиентов | MRR: {self.metrics['total_mrr']:,} руб.")
        print("=" * 70)
        print()

    def display_metrics(self):
        """Ключевые метрики"""
        print("КЛЮЧЕВЫЕ МЕТРИКИ ПОРТФЕЛЯ")
        print("-" * 50)
        
        print(f"  MRR: {self.metrics['total_mrr']:,} руб.")
        print(f"  Клиенты: {self.metrics['total_clients']}")
        print(f"  Health Score: {self.metrics['avg_health']}/100")
        print(f"  NPS: 8.0/10")
        print(f"  Клиентов в риске: {self.metrics['at_risk']}")
        print(f"  Ушедших клиентов: 0")
        print()

    def display_clients(self):
        """Таблица клиентов"""
        print("ОБЗОР КЛИЕНТСКОГО ПОРТФЕЛЯ")
        print("=" * 70)
        print("ID  Клиент                 Тип        Health  MRR          Риск    Статус")
        print("-" * 70)
        
        for client in self.clients:
            status_text = "Активный" if client["status"] == "Active" else "В риске"
            print(f"{client['id']:<3} "
                  f"{client['name'][:20]:<22} "
                  f"{client['type']:<10} "
                  f"{client['health']:<7} "
                  f"{client['mrr']:<12,} "
                  f"{client['risk']:<6}% "
                  f"{status_text:<10}")
        
        print("=" * 70)
        print()

    def display_ai_recommendations(self):
        """AI рекомендации"""
        print("AI РЕКОМЕНДАЦИИ")
        print("-" * 50)
        
        if self.metrics['at_risk'] > 0:
            print(f"[WARN] {self.metrics['at_risk']} клиентов под угрозой ухода")
            print(f"       Рекомендация: Провести emergency call сегодня")
        else:
            print("[OK] Все клиенты в порядке!")
            print("     Рекомендация: Продолжайте в том же духе")
        print()

    def display_quick_actions(self):
        """Быстрые действия"""
        print("БЫСТРЫЕ ДЕЙСТВИЯ")
        print("-" * 50)
        
        actions = [
            ("Email Campaign", "Запустить email-рассылку"),
            ("Weekly Report", "Сгенерировать отчет"),
            ("QBR Planner", "Запланировать обзоры"),
            ("Risk Review", "Анализ рисков"),
            ("Upsell Finder", "Найти кандидатов"),
            ("NPS Survey", "Опрос удовлетворенности"),
            ("Onboarding", "Проверить новых"),
            ("Export Data", "Экспорт в CSV")
        ]
        
        for i in range(0, len(actions), 2):
            title1, desc1 = actions[i]
            if i + 1 < len(actions):
                title2, desc2 = actions[i + 1]
                print(f"  {title1:<15} {desc1:<25} {title2:<15} {desc2}")
            else:
                print(f"  {title1:<15} {desc1}")
        print()

    def display_menu(self):
        """Основное меню"""
        print("ИНТЕРАКТИВНОЕ МЕНЮ")
        print("-" * 50)
        
        menu_items = [
            ("1", "Детальный анализ клиента"),
            ("2", "Генератор писем"),
            ("3", "Создать отчет"),
            ("4", "Запланировать встречи"),
            ("5", "Обновить данные"),
            ("6", "Экспорт в CSV"),
            ("7", "Настройки"),
            ("8", "Выход")
        ]
        
        for i in range(0, len(menu_items), 2):
            num1, text1 = menu_items[i]
            if i + 1 < len(menu_items):
                num2, text2 = menu_items[i + 1]
                print(f"  {num1}. {text1:<30} {num2}. {text2}")
        
        print("-" * 50)
        
        try:
            choice = input("\nВыберите действие (1-8): ").strip()
            
            if choice == "1":
                self.client_detail()
            elif choice == "2":
                self.email_generator()
            elif choice == "3":
                self.create_report()
            elif choice == "4":
                self.schedule_meetings()
            elif choice == "5":
                self.update_data()
            elif choice == "6":
                self.export_csv()
            elif choice == "7":
                self.settings()
            elif choice == "8":
                self.exit_program()
            else:
                print("\n[ERROR] Неверный выбор")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\n\n[EXIT] Программа прервана")
            sys.exit(0)

    def client_detail(self):
        """Детали клиента"""
        print("\nДЕТАЛЬНЫЙ АНАЛИЗ КЛИЕНТА")
        print("=" * 50)
        
        try:
            client_id = int(input(f"\nВведите ID клиента (1-{len(self.clients)}): "))
            client = next((c for c in self.clients if c["id"] == client_id), None)
            
            if client:
                print(f"\nКлиент: {client['name']}")
                print(f"Тип: {client['type']}")
                print(f"Health Score: {client['health']}/100")
                print(f"MRR: {client['mrr']:,} руб.")
                print(f"Риск оттока: {client['risk']}%")
                print(f"Статус: {client['status']}")
                print(f"\nКонтактная информация:")
                print(f"  Email: contact@{client['name'].split()[0].lower()}.ru")
                print(f"  Телефон: +7 (999) XXX-XX-XX")
            else:
                print("\n[ERROR] Клиент не найден")
            
            input("\nНажмите Enter для продолжения...")
            
        except ValueError:
            print("\n[ERROR] Введите число")
            time.sleep(1)

    def email_generator(self):
        """Генератор писем"""
        print("\nГЕНЕРАТОР ПИСЕМ")
        print("=" * 50)
        
        print("\nДоступные шаблоны:")
        print("  1. Приветственное письмо")
        print("  2. Follow-up после встречи")
        print("  3. Напоминание об оплате")
        print("  4. Назад")
        
        choice = input("\nВыберите шаблон (1-4): ")
        
        if choice in ["1", "2", "3"]:
            client_name = input("Имя клиента: ") or "OOO 'TermoProfit'"
            
            print("\n[OK] Письмо сгенерировано!")
            print("-" * 40)
            print(f"Тема: Пример письма для {client_name}")
            print(f"\nУважаемый(ая) {client_name},")
            print("\nЭто пример сгенерированного письма.")
            print("\nС уважением,")
            print("Иван Иванов")
            print("-" * 40)
            
            save = input("\nСохранить в файл? (y/n): ").lower()
            if save == 'y':
                filename = f"email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Тема: Пример письма для {client_name}\n\n")
                print(f"[OK] Сохранено в {filename}")
        
        input("\nНажмите Enter для продолжения...")

    def create_report(self):
        """Создание отчета"""
        print("\nСОЗДАНИЕ ОТЧЕТА")
        print("=" * 50)
        
        print("\nТипы отчетов:")
        print("  1. Еженедельный отчет")
        print("  2. Отчет по рискам")
        print("  3. Отчет по MRR")
        print("  4. Назад")
        
        choice = input("\nВыберите тип (1-4): ")
        
        if choice in ["1", "2", "3"]:
            print("\n[SYNC] Генерация отчета...")
            time.sleep(1)
            
            print("\n[OK] Отчет успешно создан!")
            print(f"Тип: {'Еженедельный' if choice == '1' else 'Рисковый' if choice == '2' else 'MRR'}")
            print(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
            print(f"Клиентов: {self.metrics['total_clients']}")
            
            filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Отчет по портфелю клиентов\n")
                f.write(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
                f.write(f"Клиентов: {self.metrics['total_clients']}\n")
                f.write(f"MRR: {self.metrics['total_mrr']:,} руб.\n")
            
            print(f"Файл: {filename}")
        
        input("\nНажмите Enter для продолжения...")

    def schedule_meetings(self):
        """Планирование встреч"""
        print("\nПЛАНИРОВАНИЕ ВСТРЕЧ")
        print("=" * 50)
        
        print("\nПредстоящие встречи:")
        for client in self.clients:
            print(f"  • {client['name']} - {datetime.now().strftime('%d.%m')}")
        
        print("\nДоступные действия:")
        print("  1. Запланировать новую встречу")
        print("  2. Назад")
        
        choice = input("\nВыберите действие (1-2): ")
        
        if choice == "1":
            print("\n[OK] Встреча запланирована!")
            print("Клиент: OOO 'TermoProfit'")
            print("Дата: 20.12.2023")
            print("Цель: Обсуждение апгрейда")
        
        input("\nНажмите Enter для продолжения...")

    def update_data(self):
        """Обновление данных"""
        print("\nОБНОВЛЕНИЕ ДАННЫХ")
        print("=" * 50)
        
        print("\n[SYNC] Обновление метрик...")
        time.sleep(1)
        
        old_mrr = self.metrics['total_mrr']
        self.metrics['total_mrr'] = sum(c["mrr"] for c in self.clients)
        
        print("\n[OK] Данные обновлены!")
        print(f"Текущий MRR: {self.metrics['total_mrr']:,} руб.")
        print(f"Активных клиентов: {self.metrics['total_clients']}")
        
        if self.metrics['total_mrr'] != old_mrr:
            change = self.metrics['total_mrr'] - old_mrr
            print(f"Изменение MRR: {change:+,} руб.")
        
        input("\nНажмите Enter для продолжения...")

    def export_csv(self):
        """Экспорт в CSV"""
        print("\nЭКСПОРТ В CSV")
        print("=" * 50)
        
        filename = f"csm_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        try:
            print("\n[SAVE] Экспорт данных...")
            time.sleep(1)
            
            with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                fieldnames = ['ID', 'Name', 'Type', 'Health', 'MRR', 'Risk', 'Status']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for client in self.clients:
                    writer.writerow({
                        'ID': client['id'],
                        'Name': client['name'],
                        'Type': client['type'],
                        'Health': client['health'],
                        'MRR': client['mrr'],
                        'Risk': f"{client['risk']}%",
                        'Status': client['status']
                    })
            
            print("\n[OK] Данные успешно экспортированы!")
            print(f"Файл: {filename}")
            print(f"Записей: {len(self.clients)}")
            
            preview = input("\nПоказать первые 3 строки? (y/n): ").lower()
            if preview == 'y':
                print("\nПРЕДПРОСМОТР:")
                with open(filename, 'r', encoding='utf-8-sig') as f:
                    for i, line in enumerate(f):
                        if i < 4:
                            print(f"  {line.strip()}")
            
        except Exception as e:
            print(f"\n[ERROR] Ошибка экспорта: {e}")
        
        input("\nНажмите Enter для продолжения...")

    def settings(self):
        """Настройки"""
        print("\nНАСТРОЙКИ")
        print("=" * 50)
        
        print("\nТекущие настройки:")
        print("  Тема: Стандартная")
        print("  Язык: Русский")
        print("  Формат даты: DD.MM.YYYY")
        print("  Валюта: RUB (руб.)")
        print("  Версия: 3.5")
        
        print("\nДоступные действия:")
        print("  1. Сменить тему")
        print("  2. Настроить уведомления")
        print("  3. Назад")
        
        choice = input("\nВыберите действие (1-3): ")
        
        if choice in ["1", "2"]:
            print("\n[INFO] Функция в разработке...")
            print("Ожидайте в следующем обновлении v3.6!")
        
        input("\nНажмите Enter для продолжения...")

    def exit_program(self):
        """Выход из программы"""
        print("\nВЫХОД ИЗ ПРОГРАММЫ")
        print("=" * 50)
        
        print("\n[SAVE] Сохранение данных...")
        time.sleep(1)
        
        print("\n[OK] Статистика за сессию:")
        print(f"  • Клиентов просмотрено: {len(self.clients)}")
        print(f"  • Общий MRR: {self.metrics['total_mrr']:,} руб.")
        print(f"  • Средний Health Score: {self.metrics['avg_health']}")
        print(f"  • Клиентов в риске: {self.metrics['at_risk']}")
        
        print("\nСпасибо за использование CSM Dashboard Pro!")
        time.sleep(2)
        sys.exit(0)

    def run(self):
        """Основной цикл"""
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                display_logo()
                self.display_header()
                self.display_metrics()
                self.display_clients()
                self.display_ai_recommendations()
                self.display_quick_actions()
                self.display_menu()
                
            except Exception as e:
                print(f"\n[ERROR] Неожиданная ошибка: {e}")
                time.sleep(2)
                continue

# ================== ЗАПУСК ==================
if __name__ == "__main__":
    try:
        print("=" * 70)
        print("ЗАПУСК CSM DASHBOARD PRO v3.5")
        print("=" * 70)
        
        time.sleep(1)
        
        app = Dashboard()
        app.run()
        
    except KeyboardInterrupt:
        print("\n[EXIT] Программа завершена")
    except Exception as e:
        print(f"\n[ERROR] Критическая ошибка: {e}")
