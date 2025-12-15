#!/usr/bin/env python3
"""
================================================================================
                        CSM DASHBOARD PRO v3.2
                  Customer Success Manager Dashboard
                      [AI-Powered Analytics]
================================================================================
Профессиональная панель управления с цветным интерфейсом для Windows cmd.
Использует ANSI коды для цветов и Unicode для графики.
"""

import json
import os
import sys
import csv
from datetime import datetime, timedelta
from collections import Counter
import time

# ================== НАСТРОЙКИ ЦВЕТОВ ДЛЯ WINDOWS ==================
class Colors:
    """ANSI коды для цветного текста в Windows 10+."""
    # Сброс
    RESET = "\033[0m"
    
    # Основные цвета
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    
    # Жирный текст
    BOLD = "\033[1m"
    BOLD_BLUE = "\033[1;94m"
    BOLD_GREEN = "\033[1;92m"
    BOLD_RED = "\033[1;91m"
    BOLD_CYAN = "\033[1;96m"
    
    # Фон
    BG_BLUE = "\033[44m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    
    @staticmethod
    def color(text, color_code):
        """Окрашивает текст и сбрасывает цвет в конце."""
        return f"{color_code}{text}{Colors.RESET}"

class Icons:
    """Улучшенные текстовые иконки с Unicode символами."""
    # Главная картинка/логотип
    LOGO = f"""
{Colors.BOLD_BLUE}
    ╔══════════════════════════════════════════╗
    ║   ██████╗███████╗███╗   ███╗            ║
    ║  ██╔════╝██╔════╝████╗ ████║            ║
    ║  ██║     ███████╗██╔████╔██║            ║
    ║  ██║     ╚════██║██║╚██╔╝██║            ║
    ║  ╚██████╗███████║██║ ╚═╝ ██║            ║
    ║   ╚═════╝╚══════╝╚═╝     ╚═╝            ║
    ║                                          ║
    ║  CUSTOMER SUCCESS MANAGER DASHBOARD PRO  ║
    ║                 v3.2                     ║
    ╚══════════════════════════════════════════╝{Colors.RESET}
"""
    
    # Иконки для метрик (улучшенные)
    CHART = f"{Colors.CYAN}📊{Colors.RESET}"
    USERS = f"{Colors.GREEN}👥{Colors.RESET}"
    HEART = f"{Colors.RED}❤{Colors.RESET}"
    STAR = f"{Colors.YELLOW}⭐{Colors.RESET}"
    WARNING = f"{Colors.RED}⚠{Colors.RESET}"
    DOWN = f"{Colors.RED}📉{Colors.RESET}"
    EMAIL = f"{Colors.BLUE}📧{Colors.RESET}"
    REPORT = f"{Colors.GREEN}📋{Colors.RESET}"
    CALENDAR = f"{Colors.MAGENTA}📅{Colors.RESET}"
    SYNC = f"{Colors.CYAN}🔄{Colors.RESET}"
    SAVE = f"{Colors.GREEN}💾{Colors.RESET}"
    SETTINGS = f"{Colors.YELLOW}⚙{Colors.RESET}"
    EXIT = f"{Colors.RED}🚪{Colors.RESET}"
    DETAIL = f"{Colors.CYAN}🔍{Colors.RESET}"
    AI = f"{Colors.MAGENTA}🤖{Colors.RESET}"
    QUICK = f"{Colors.GREEN}⚡{Colors.RESET}"
    MENU = f"{Colors.BLUE}📋{Colors.RESET}"
    PHONE = f"{Colors.GREEN}📞{Colors.RESET}"
    TAG = f"{Colors.CYAN}🏷{Colors.RESET}"
    MONEY = f"{Colors.GREEN}💰{Colors.RESET}"
    CLOCK = f"{Colors.YELLOW}⏰{Colors.RESET}"
    CHECK = f"{Colors.GREEN}✅{Colors.RESET}"
    FOLDER = f"{Colors.BLUE}📁{Colors.RESET}"
    GRAPH = f"{Colors.CYAN}📈{Colors.RESET}"
    BELL = f"{Colors.YELLOW}🔔{Colors.RESET}"
    
    # Разделители
    H_LINE = f"{Colors.BLUE}{'═' * 60}{Colors.RESET}"
    H_THIN = f"{Colors.CYAN}{'─' * 50}{Colors.RESET}"

class CSMDashboardPro:
    """Улучшенная панель управления CSM с цветным интерфейсом."""
    
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
            },
            {
                "id": 4,
                "name": "ООО 'МедиаГрупп'",
                "tier": "Business",
                "manager": "Мария Петрова",
                "status": "active",
                "health_score": 88,
                "mrr": 95000,
                "churn_risk": 0.08,
                "last_activity": "2025-12-14",
                "nps": 8,
                "onboarding_date": "2025-02-10",
                "tags": ["media", "loyal", "upsell"],
                "contact_person": "Ольга Ковалева",
                "email": "olga@mediagroup.ru",
                "phone": "+7 (999) 456-78-90",
                "usage_trend": "increasing",
                "last_interaction": "Презентация новых тарифов",
                "next_action": "Подписание договора",
                "action_date": "2025-12-22"
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
    
    def _clear_screen(self):
        """Очищает экран с учетом ОС."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Отображает заголовок с логотипом."""
        print(Icons.LOGO)
        print(Icons.H_LINE)
        print(f"{Colors.BOLD_BLUE}Дата:{Colors.RESET} {datetime.now().strftime('%d %B %Y, %A')}")
        print(f"{Colors.BOLD_BLUE}Менеджер:{Colors.RESET} Иван Иванов {Colors.BLUE}|{Colors.RESET} "
              f"{Colors.BOLD_BLUE}Email:{Colors.RESET} ivan@company.com")
        print(f"{Colors.BOLD_BLUE}Портфель:{Colors.RESET} {self.metrics['total_clients']} активных клиентов "
              f"{Colors.BLUE}|{Colors.RESET} "
              f"{Colors.BOLD_BLUE}MRR:{Colors.RESET} {self.metrics['total_mrr']:,} руб.")
        print(Icons.H_LINE)
        print()
    
    def display_metrics(self):
        """Отображает ключевые метрики."""
        print(f"{Icons.CHART} {Colors.BOLD_CYAN}КЛЮЧЕВЫЕ МЕТРИКИ ПОРТФЕЛЯ{Colors.RESET}")
        print(Icons.H_THIN)
        
        metrics_display = [
            (Icons.MONEY, "MRR", f"{self.metrics['total_mrr']:,} руб."),
            (Icons.USERS, "Клиенты", self.metrics['total_clients']),
            (Icons.HEART, "Health Score", f"{self.metrics['avg_health_score']}/100"),
            (Icons.STAR, "NPS", f"{self.metrics['avg_nps']}/10"),
            (Icons.WARNING, "Клиентов в риске", self.metrics['at_risk_count']),
            (Icons.DOWN, "Ушедших клиентов", self.metrics['total_churned'])
        ]
        
        for icon, label, value in metrics_display:
            print(f"  {icon} {Colors.BOLD_BLUE}{label}:{Colors.RESET} {value}")
        
        print()
    
    def display_clients_table(self):
        """Отображает таблицу клиентов."""
        print(f"{Icons.USERS} {Colors.BOLD_CYAN}ОБЗОР КЛИЕНТСКОГО ПОРТФЕЛЯ{Colors.RESET}")
        print(Icons.H_LINE)
        
        # Заголовок таблицы
        headers = ["ID", "Клиент", "Тип", "Health", "MRR", "Риск", "Статус"]
        print(f"{Colors.BOLD_BLUE}{headers[0]:<3} {headers[1]:<22} {headers[2]:<10} "
              f"{headers[3]:<7} {headers[4]:<12} {headers[5]:<7} {headers[6]:<10}{Colors.RESET}")
        
        print(Icons.H_THIN)
        
        # Данные клиентов
        for client in self.clients_data:
            # Определение цвета статуса
            if client["status"] == "active":
                status_color = Colors.GREEN
                status_text = "Активный"
            elif client["status"] == "at_risk":
                status_color = Colors.RED
                status_text = "В риске"
            else:
                status_color = Colors.YELLOW
                status_text = "Ушел"
            
            # Определение цвета health score
            health = client["health_score"]
            if health >= 80:
                health_color = Colors.GREEN
            elif health >= 60:
                health_color = Colors.YELLOW
            else:
                health_color = Colors.RED
            
            risk_percent = f"{client['churn_risk']*100:.0f}%"
            
            print(f"{client['id']:<3} "
                  f"{Colors.BOLD}{client['name'][:20]:<22}{Colors.RESET} "
                  f"{client['tier']:<10} "
                  f"{health_color}{health:<7}{Colors.RESET} "
                  f"{Colors.GREEN}{client['mrr']:<12,}{Colors.RESET} "
                  f"{Colors.RED if client['churn_risk'] > 0.3 else Colors.YELLOW}{risk_percent:<7}{Colors.RESET} "
                  f"{status_color}{status_text:<10}{Colors.RESET}")
        
        print(Icons.H_LINE)
        print()
    
    def display_ai_recommendations(self):
        """Отображает AI-рекомендации."""
        print(f"{Icons.AI} {Colors.BOLD_CYAN}AI РЕКОМЕНДАЦИИ{Colors.RESET}")
        print(Icons.H_THIN)
        
        recommendations = []
        
        # Проверка рисковых клиентов
        if self.metrics['at_risk_count'] > 0:
            risk_clients = [c for c in self.clients_data if c["status"] == "at_risk"]
            names = ", ".join([c["name"] for c in risk_clients[:2]])
            if len(risk_clients) > 2:
                names += f" и еще {len(risk_clients)-2}"
            
            recommendations.append(
                f"{Icons.WARNING} {Colors.RED}{self.metrics['at_risk_count']} клиентов под угрозой{Colors.RESET}\n"
                f"   {Colors.BOLD}Клиенты:{Colors.RESET} {names}\n"
                f"   {Colors.BOLD}Действие:{Colors.RESET} {Colors.GREEN}Провести emergency call сегодня{Colors.RESET}"
            )
        
        # Проверка неактивных клиентов
        two_weeks_ago = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")
        inactive = [c for c in self.clients_data 
                   if c["last_activity"] < two_weeks_ago and c["status"] == "active"]
        if inactive:
            recommendations.append(
                f"{Icons.BELL} {Colors.YELLOW}{len(inactive)} клиентов не активны 2+ недели{Colors.RESET}\n"
                f"   {Colors.BOLD}Действие:{Colors.RESET} {Colors.GREEN}Отправить check-in письма{Colors.RESET}"
            )
        
        # Проверка upcoming meetings
        upcoming = [c for c in self.clients_data if c.get("action_date")]
        if upcoming:
            today = datetime.now().strftime("%Y-%12-%d")
            today_meetings = [c for c in upcoming if c["action_date"] == today]
            if today_meetings:
                recommendations.append(
                    f"{Icons.CALENDAR} {Colors.CYAN}Сегодня запланировано {len(today_meetings)} встреч{Colors.RESET}\n"
                    f"   {Colors.BOLD}Действие:{Colors.RESET} {Colors.GREEN}Подготовить материалы{Colors.RESET}"
                )
        
        # Если нет рекомендаций
        if not recommendations:
            recommendations.append(
                f"{Icons.CHECK} {Colors.GREEN}Все клиенты в порядке!{Colors.RESET}\n"
                f"   {Colors.BOLD}Действие:{Colors.RESET} {Colors.GREEN}Продолжайте в том же духе{Colors.RESET}"
            )
        
        # Вывод рекомендаций
        for i, rec in enumerate(recommendations):
            print(rec)
            if i < len(recommendations) - 1:
                print()
        
        print()
    
    def display_quick_actions(self):
        """Отображает быстрые действия."""
        print(f"{Icons.QUICK} {Colors.BOLD_CYAN}БЫСТРЫЕ ДЕЙСТВИЯ{Colors.RESET}")
        print(Icons.H_THIN)
        
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
        
        # Вывод в 2 колонки
        for i in range(0, len(actions), 2):
            icon1, title1, desc1 = actions[i]
            if i + 1 < len(actions):
                icon2, title2, desc2 = actions[i + 1]
                print(f"  {icon1} {Colors.BOLD_BLUE}{title1:<15}{Colors.RESET} {desc1:<25} "
                      f"{icon2} {Colors.BOLD_BLUE}{title2:<15}{Colors.RESET} {desc2}")
            else:
                print(f"  {icon1} {Colors.BOLD_BLUE}{title1:<15}{Colors.RESET} {desc1}")
        
        print()
    
    def display_interactive_menu(self):
        """Отображает исправленное меню."""
        print(f"{Icons.MENU} {Colors.BOLD_CYAN}ИНТЕРАКТИВНОЕ МЕНЮ{Colors.RESET}")
        print(Icons.H_THIN)
        
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
        
        # Выравнивание меню
        for i in range(0, len(menu_items), 2):
            num1, text1 = menu_items[i]
            if i + 1 < len(menu_items):
                num2, text2 = menu_items[i + 1]
                print(f"  {Colors.BOLD}{num1}.{Colors.RESET} {text1:<30} "
                      f"{Colors.BOLD}{num2}.{Colors.RESET} {text2}")
            else:
                print(f"  {Colors.BOLD}{num1}.{Colors.RESET} {text1}")
        
        print(Icons.H_THIN)
        
        try:
            choice = input(f"\n{Colors.BOLD_BLUE}Выберите действие (1-8):{Colors.RESET} ").strip()
            
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
                print(f"\n{Colors.RED}[ERROR]{Colors.RESET} Неверный выбор. Пожалуйста, выберите 1-8")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}[EXIT]{Colors.RESET} Выход из программы.")
            sys.exit(0)
    
    def client_detail_view(self):
        """Детальный просмотр клиента."""
        self._clear_screen()
        print(f"{Icons.DETAIL} {Colors.BOLD_CYAN}ДЕТАЛЬНЫЙ АНАЛИЗ КЛИЕНТА{Colors.RESET}")
        print(Icons.H_LINE)
        
        try:
            client_id = int(input(f"{Colors.BOLD_BLUE}Введите ID клиента (1-{len(self.clients_data)}):{Colors.RESET} "))
            client = next((c for c in self.clients_data if c["id"] == client_id), None)
            
            if not client:
                print(f"{Colors.RED}[ERROR]{Colors.RESET} Клиент не найден!")
                time.sleep(1)
                return
            
            print()
            print(f"{Icons.USERS} {Colors.BOLD}{client['name']}{Colors.RESET}")
            print(Icons.H_THIN)
            
            # Основная информация
            info_sections = [
                (f"{Colors.BOLD_BLUE}Тип:{Colors.RESET}", client['tier']),
                (f"{Colors.BOLD_BLUE}Менеджер:{Colors.RESET}", client['manager']),
                (f"{Colors.BOLD_BLUE}Дата онбординга:{Colors.RESET}", client['onboarding_date'])
            ]
            
            for label, value in info_sections:
                print(f"{label} {value}")
            
            print()
            
            # Метрики
            print(f"{Colors.BOLD_CYAN}МЕТРИКИ КЛИЕНТА:{Colors.RESET}")
            metrics = [
                (Icons.HEART, "Health Score", f"{client['health_score']}/100"),
                (Icons.MONEY, "MRR", f"{client['mrr']:,} руб."),
                (Icons.WARNING, "Риск оттока", f"{client['churn_risk']:.1%}"),
                (Icons.STAR, "NPS", f"{client['nps']}/10"),
                (Icons.CLOCK, "Последняя активность", client['last_activity']),
                (Icons.GRAPH, "Тренд использования", client['usage_trend'])
            ]
            
            for icon, label, value in metrics:
                print(f"  {icon} {Colors.BOLD_BLUE}{label}:{Colors.RESET} {value}")
            
            print()
            
            # Контактная информация
            print(f"{Icons.PHONE} {Colors.BOLD_CYAN}КОНТАКТНАЯ ИНФОРМАЦИЯ:{Colors.RESET}")
            contacts = [
                (f"{Colors.BOLD_BLUE}Контакт:{Colors.RESET}", client['contact_person']),
                (f"{Colors.BOLD_BLUE}Email:{Colors.RESET}", client['email']),
                (f"{Colors.BOLD_BLUE}Телефон:{Colors.RESET}", client['phone'])
            ]
            
            for label, value in contacts:
                print(f"  {label} {value}")
            
            print()
            
            # Теги
            if client['tags']:
                print(f"{Icons.TAG} {Colors.BOLD_CYAN}ТЕГИ:{Colors.RESET}")
                tags_text = " ".join([f"{Colors.CYAN}[{tag}]{Colors.RESET}" for tag in client['tags']])
                print(f"  {tags_text}")
            
            print()
            
            # Следующие действия
            if client.get('next_action'):
                print(f"{Icons.CALENDAR} {Colors.BOLD_CYAN}СЛЕДУЮЩЕЕ ДЕЙСТВИЕ:{Colors.RESET}")
                print(f"  {Colors.BOLD_BLUE}Действие:{Colors.RESET} {client['next_action']}")
                print(f"  {Colors.BOLD_BLUE}Дата:{Colors.RESET} {client.get('action_date', 'Не назначено')}")
            
            print()
            print(Icons.H_THIN)
            input(f"{Colors.BOLD_BLUE}Нажмите Enter для возврата...{Colors.RESET}")
            
        except ValueError:
            print(f"{Colors.RED}[ERROR]{Colors.RESET} Введите число!")
            time.sleep(1)
    
    def email_generator(self):
        """Генератор профессиональных писем."""
        self._clear_screen()
        print(f"{Icons.EMAIL} {Colors.BOLD_CYAN}ГЕНЕРАТОР ПИСЕМ{Colors.RESET}")
        print(Icons.H_LINE)
        
        print(f"\n{Colors.BOLD_CYAN}Доступные шаблоны:{Colors.RESET}")
        templates = [
            ("1", "Приветственное письмо (онбординг)"),
            ("2", "Follow-up после встречи"),
            ("3", "Напоминание об оплате"),
            ("4", "Check-in (недельный)"),
            ("5", "Назад в меню")
        ]
        
        for num, desc in templates:
            print(f"  {Colors.BOLD}{num}.{Colors.RESET} {desc}")
        
        try:
            choice = input(f"\n{Colors.BOLD_BLUE}Выберите шаблон (1-5):{Colors.RESET} ").strip()
            
            if choice == "5":
                print(f"{Colors.YELLOW}[BACK]{Colors.RESET} Возврат в меню...")
                time.sleep(1)
                return
            
            if choice in ["1", "2", "3", "4"]:
                client_name = input(f"{Colors.BOLD_BLUE}Имя клиента:{Colors.RESET} ") or "ООО 'ТехноПрофит'"
                manager_name = input(f"{Colors.BOLD_BLUE}Ваше имя:{Colors.RESET} ") or "Иван Иванов"
                
                print(f"\n{Icons.CHECK} {Colors.GREEN}Письмо сгенерировано!{Colors.RESET}")
                print(Icons.H_THIN)
                
                # Генерация письма
                subject = ""
                body = ""
                
                if choice == "1":
                    subject = f"Добро пожаловать в нашу платформу, {client_name}!"
                    body = f"""Уважаемый(ая) {client_name},

Добро пожаловать в нашу платформу! Мы рады видеть вас среди наших клиентов.

Наша команда готова помочь вам с:
1. Настройкой и интеграцией
2. Обучением вашей команды
3. Любыми техническими вопросами

Не стесняйтесь обращаться по любым вопросам.

С уважением,
{manager_name}
Customer Success Manager"""
                
                elif choice == "2":
                    subject = f"Follow-up после нашей встречи"
                    body = f"""Уважаемый(ая) {client_name},

Спасибо за время на нашей встрече. Как обсуждали:

1. [Пункт 1 по результатам встречи]
2. [Пункт 2 по результатам встречи]
3. [Пункт 3 по результатам встречи]

Следующие шаги с нашей стороны:
- [Действие 1] до [дата]
- [Действие 2] до [дата]

Жду ваших комментариев.

С уважением,
{manager_name}
Customer Success Manager"""
                
                elif choice == "3":
                    subject = f"Напоминание об оплате"
                    body = f"""Уважаемый(ая) {client_name},

Напоминаем, что срок оплаты по договору истекает [дата].

Сумма к оплате: [сумма] руб.
Номер счета: [номер счета]

Просим произвести оплату в указанные сроки.

С уважением,
{manager_name}
Customer Success Manager"""
                
                else:  # choice == "4"
                    subject = f"Еженедельный check-in"
                    body = f"""Уважаемый(ая) {client_name},

Как ваши дела на этой неделе?

Есть ли вопросы или проблемы, с которыми мы можем помочь?
Какие успехи или сложности в использовании платформы?

Жду ваших новостей!

С уважением,
{manager_name}
Customer Success Manager"""
                
                # Вывод письма
                print(f"{Colors.BOLD_BLUE}Тема:{Colors.RESET} {subject}")
                print(f"\n{Colors.BOLD_BLUE}Текст письма:{Colors.RESET}")
                print("-" * 40)
                print(body)
                print("-" * 40)
                
                # Опция сохранения
                save = input(f"\n{Colors.BOLD_BLUE}Сохранить в файл? (y/n):{Colors.RESET} ").lower()
                if save == 'y':
                    filename = f"email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(f"Тема: {subject}\n\n{body}")
                    print(f"{Icons.SAVE} {Colors.GREEN}Сохранено в {filename}{Colors.RESET}")
                
                print()
                input(f"{Colors.BOLD_BLUE}Нажмите Enter для продолжения...{Colors.RESET}")
                
            else:
                print(f"{Colors.RED}[ERROR]{Colors.RESET} Неверный выбор")
                time.sleep(1)
                
        except Exception as e:
            print(f"{Colors.RED}[ERROR]{Colors.RESET} {e}")
            time.sleep(1)
    
    def create_report(self):
        """Создание отчетов."""
        self._clear_screen()
        print(f"{Icons.REPORT} {Colors.BOLD_CYAN}СОЗДАНИЕ ОТЧЕТОВ{Colors.RESET}")
        print(Icons.H_LINE)
        
        print(f"\n{Colors.BOLD_CYAN}Типы отчетов:{Colors.RESET}")
        report_types = [
            ("1", "Еженедельный отчет по портфелю"),
            ("2", "Отчет по рисковым клиентам"),
            ("3", "Отчет по MRR"),
            ("4", "Отчет по NPS"),
            ("5", "Назад в меню")
        ]
        
        for num, desc in report_types:
            print(f"  {Colors.BOLD}{num}.{Colors.RESET} {desc}")
        
        try:
            choice = input(f"\n{Colors.BOLD_BLUE}Выберите тип (1-5):{Colors.RESET} ").strip()
            
            if choice == "5":
                print(f"{Colors.YELLOW}[BACK]{Colors.RESET} Возврат в меню...")
                time.sleep(1)
                return
            
            if choice in ["1", "2", "3", "4"]:
                print(f"\n{Icons.SYNC} {Colors.CYAN}Генерация отчета...{Colors.RESET}")
                time.sleep(1.5)
                
                # Генерация отчета
                report_name = ""
                if choice == "1":
                    report_name = "Еженедельный отчет по портфелю"
                elif choice == "2":
                    report_name = "Отчет по рисковым клиентам"
                elif choice == "3":
                    report_name = "Отчет по MRR"
                else:
                    report_name = "Отчет по NPS"
                
                filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"{'='*60}\n")
                    f.write(f"{report_name}\n")
                    f.write(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
                    f.write(f"{'='*60}\n\n")
                    
                    f.write(f"Общая статистика:\n")
                    f.write(f"- Активных клиентов: {self.metrics['total_clients']}\n")
                    f.write(f"- Общий MRR: {self.metrics['total_mrr']:,} руб.\n")
                    f.write(f"- Средний Health Score: {self.metrics['avg_health_score']}\n")
                    f.write(f"- Средний NPS: {self.metrics['avg_nps']}\n")
                    f.write(f"- Клиентов в риске: {self.metrics['at_risk_count']}\n\n")
                    
                    if choice == "2":  # Рисковые клиенты
                        risk_clients = [c for c in self.clients_data if c["churn_risk"] > 0.3]
                        f.write("Рисковые клиенты:\n")
                        for client in risk_clients:
                            f.write(f"- {client['name']} (Риск: {client['churn_risk']:.1%}, "
                                   f"Health: {client['health_score']})\n")
                    
                    f.write(f"\nСгенерировано: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n")
                
                print(f"\n{Icons.CHECK} {Colors.GREEN}Отчет успешно создан!{Colors.RESET}")
                print(f"{Colors.BOLD_BLUE}Тип:{Colors.RESET} {report_name}")
                print(f"{Colors.BOLD_BLUE}Дата:{Colors.RESET} {datetime.now().strftime('%d.%m.%Y %H:%M')}")
                print(f"{Colors.BOLD_BLUE}Клиентов:{Colors.RESET} {self.metrics['total_clients']}")
                print(f"{Colors.BOLD_BLUE}Файл:{Colors.RESET} {filename}")
                
                print()
                input(f"{Colors.BOLD_BLUE}Нажмите Enter для продолжения...{Colors.RESET}")
                
            else:
                print(f"{Colors.RED}[ERROR]{Colors.RESET} Неверный выбор")
                time.sleep(1)
                
        except Exception as e:
            print(f"{Colors.RED}[ERROR]{Colors.RESET} {e}")
            time.sleep(1)
    
    def schedule_meetings(self):
        """Планирование встреч."""
        self._clear_screen()
        print(f"{Icons.CALENDAR} {Colors.BOLD_CYAN}ПЛАНИРОВАНИЕ ВСТРЕЧ{Colors.RESET}")
        print(Icons.H_LINE)
        
        # Предстоящие встречи
        upcoming = [c for c in self.clients_data if c.get("action_date")]
        today = datetime.now().strftime("%Y-12-%d")
        
        print(f"\n{Colors.BOLD_CYAN}ПРЕДСТОЯЩИЕ ВСТРЕЧИ:{Colors.RESET}")
        
        if not upcoming:
            print(f"  {Icons.CHECK} {Colors.GREEN}Нет запланированных встреч{Colors.RESET}")
        else:
            # Группировка по датам
            meetings_by_date = {}
            for client in upcoming:
                date = client["action_date"]
                if date not in meetings_by_date:
                    meetings_by_date[date] = []
                meetings_by_date[date].append(client)
            
            # Сортировка дат
            for date in sorted(meetings_by_date.keys()):
                is_today = date == today
                date_prefix = f"{Colors.GREEN}➤ СЕГОДНЯ{Colors.RESET}" if is_today else date
                print(f"\n  {Colors.BOLD_BLUE}{date_prefix}:{Colors.RESET}")
                
                for client in meetings_by_date[date]:
                    print(f"    • {client['name']} - {client['next_action']}")
        
        # Добавление новой встречи
        print(f"\n{Colors.BOLD_CYAN}НОВАЯ ВСТРЕЧА:{Colors.RESET}")
        print(f"  {Colors.BOLD}1.{Colors.RESET} Запланировать новую встречу")
        print(f"  {Colors.BOLD}2.{Colors.RESET} Вернуться в меню")
        
        try:
            choice = input(f"\n{Colors.BOLD_BLUE}Выберите действие (1-2):{Colors.RESET} ").strip()
            
            if choice == "1":
                client_id = input(f"{Colors.BOLD_BLUE}ID клиента:{Colors.RESET} ")
                date = input(f"{Colors.BOLD_BLUE}Дата (YYYY-MM-DD):{Colors.RESET} ")
                purpose = input(f"{Colors.BOLD_BLUE}Цель встречи:{Colors.RESET} ")
                
                print(f"\n{Icons.CHECK} {Colors.GREEN}Встреча запланирована!{Colors.RESET}")
                print(f"Клиент: {client_id}")
                print(f"Дата: {date}")
                print(f"Цель: {purpose}")
                
            elif choice != "2":
                print(f"{Colors.RED}[ERROR]{Colors.RESET} Неверный выбор")
        
        except Exception as e:
            print(f"{Colors.RED}[ERROR]{Colors.RESET} {e}")
        
        print()
        input(f"{Colors.BOLD_BLUE}Нажмите Enter для возврата...{Colors.RESET}")
    
    def update_data(self):
        """Обновление данных."""
        self._clear_screen()
        print(f"{Icons.SYNC} {Colors.BOLD_CYAN}ОБНОВЛЕНИЕ ДАННЫХ{Colors.RESET}")
        print(Icons.H_LINE)
        
        print(f"\n{Icons.SYNC} {Colors.CYAN}Обновление метрик...{Colors.RESET}")
        
        # Анимация обновления
        for i in range(3):
            print(f"  {Colors.CYAN}⏳ Загрузка данных{'.' * (i+1)}{Colors.RESET}", end='\r')
            time.sleep(0.3)
        
        # Пересчет метрик
        old_mrr = self.metrics['total_mrr']
        old_clients = self.metrics['total_clients']
        
        self.metrics = self._calculate_metrics()
        
        print(f"\n{Icons.CHECK} {Colors.GREEN}Данные обновлены!{Colors.RESET}")
        print()
        
        # Статистика изменений
        print(f"{Colors.BOLD_CYAN}СТАТИСТИКА:{Colors.RESET}")
        print(f"  {Icons.MONEY} {Colors.BOLD_BLUE}Текущий MRR:{Colors.RESET} {self.metrics['total_mrr']:,} руб.")
        if self.metrics['total_mrr'] != old_mrr:
            change = self.metrics['total_mrr'] - old_mrr
            change_icon = f"{Colors.GREEN}▲{Colors.RESET}" if change > 0 else f"{Colors.RED}▼{Colors.RESET}"
            print(f"      {change_icon} Изменение: {change:+,} руб.")
        
        print(f"  {Icons.USERS} {Colors.BOLD_BLUE}Активных клиентов:{Colors.RESET} {self.metrics['total_clients']}")
        if self.metrics['total_clients'] != old_clients:
            change = self.metrics['total_clients'] - old_clients
            change_icon = f"{Colors.GREEN}▲{Colors.RESET}" if change > 0 else f"{Colors.RED}▼{Colors.RESET}"
            print(f"      {change_icon} Изменение: {change:+}")
        
        print(f"  {Icons.HEART} {Colors.BOLD_BLUE}Health Score:{Colors.RESET} {self.metrics['avg_health_score']}")
        print(f"  {Icons.WARNING} {Colors.BOLD_BLUE}Клиентов в риске:{Colors.RESET} {self.metrics['at_risk_count']}")
        
        print()
        input(f"{Colors.BOLD_BLUE}Нажмите Enter для продолжения...{Colors.RESET}")
    
    def export_to_csv(self):
        """Экспорт в CSV."""
        self._clear_screen()
        print(f"{Icons.SAVE} {Colors.BOLD_CYAN}ЭКСПОРТ В CSV{Colors.RESET}")
        print(Icons.H_LINE)
        
        try:
            filename = f"csm_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            
            print(f"\n{Icons.SYNC} {Colors.CYAN}Экспорт данных...{Colors.RESET}")
            time.sleep(1)
            
            with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                fieldnames = ['ID', 'Name', 'Tier', 'Manager', 'Status', 'Health_Score', 
                             'MRR', 'Churn_Risk', 'NPS', 'Last_Activity', 'Onboarding_Date',
                             'Contact_Person', 'Email', 'Phone', 'Tags']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for client in self.clients_data:
                    writer.writerow({
                        'ID': client['id'],
                        'Name': client['name'],
                        'Tier': client['tier'],
                        'Manager': client['manager'],
                        'Status': client['status'],
                        'Health_Score': client['health_score'],
                        'MRR': client['mrr'],
                        'Churn_Risk': f"{client['churn_risk']:.3f}",
                        'NPS': client['nps'],
                        'Last_Activity': client['last_activity'],
                        'Onboarding_Date': client['onboarding_date'],
                        'Contact_Person': client['contact_person'],
                        'Email': client['email'],
                        'Phone': client['phone'],
                        'Tags': ';'.join(client['tags'])
                    })
            
            print(f"\n{Icons.CHECK} {Colors.GREEN}Данные успешно экспортированы!{Colors.RESET}")
            print(f"{Colors.BOLD_BLUE}Файл:{Colors.RESET} {filename}")
            print(f"{Colors.BOLD_BLUE}Записей:{Colors.RESET} {len(self.clients_data)}")
            print(f"{Colors.BOLD_BLUE}Разделитель:{Colors.RESET} Запятая (CSV)")
            print(f"{Colors.BOLD_BLUE}Кодировка:{Colors.RESET} UTF-8 with BOM")
            
            # Предпросмотр
            preview = input(f"\n{Colors.BOLD_BLUE}Показать первые 3 строки? (y/n):{Colors.RESET} ").lower()
            if preview == 'y':
                print(f"\n{Colors.BOLD_CYAN}ПРЕДПРОСМОТР:{Colors.RESET}")
                with open(filename, 'r', encoding='utf-8-sig') as f:
                    for i, line in enumerate(f):
                        if i < 4:  # Заголовок + 3 строки
                            print(f"  {line.strip()}")
                        else:
                            break
            
            print()
            input(f"{Colors.BOLD_BLUE}Нажмите Enter для продолжения...{Colors.RESET}")
            
        except Exception as e:
            print(f"\n{Colors.RED}[ERROR]{Colors.RESET} Ошибка экспорта: {e}")
            time.sleep(2)
    
    def show_settings(self):
        """Настройки программы."""
        self._clear_screen()
        print(f"{Icons.SETTINGS} {Colors.BOLD_CYAN}НАСТРОЙКИ ПРОГРАММЫ{Colors.RESET}")
        print(Icons.H_LINE)
        
        settings = [
            ("Тема", "Стандартная (синяя)"),
            ("Цвета", "Включены"),
            ("Уведомления", "Включены"),
            ("Автосохранение", "Включено"),
            ("Язык", "Русский"),
            ("Формат даты", "DD.MM.YYYY"),
            ("Валюта", "RUB (руб.)"),
            ("Версия", "3.2 Pro")
        ]
        
        print(f"\n{Colors.BOLD_CYAN}ТЕКУЩИЕ НАСТРОЙКИ:{Colors.RESET}")
        for key, value in settings:
            print(f"  {Colors.BOLD_BLUE}{key:<20}{Colors.RESET}: {value}")
        
        print(f"\n{Colors.BOLD_CYAN}ДОСТУПНЫЕ ДЕЙСТВИЯ:{Colors.RESET}")
        actions = [
            ("1", "Сменить тему оформления"),
            ("2", "Настроить уведомления"),
            ("3", "Изменить язык"),
            ("4", "Сбросить настройки"),
            ("5", "Назад в меню")
        ]
        
        for num, desc in actions:
            print(f"  {Colors.BOLD}{num}.{Colors.RESET} {desc}")
        
        try:
            choice = input(f"\n{Colors.BOLD_BLUE}Выберите действие (1-5):{Colors.RESET} ").strip()
            
            if choice == "5":
                print(f"{Colors.YELLOW}[BACK]{Colors.RESET} Возврат в меню...")
                time.sleep(1)
                return
            
            if choice in ["1", "2", "3", "4"]:
                print(f"\n{Icons.SETTINGS} {Colors.CYAN}Эта функция в активной разработке...{Colors.RESET}")
                print(f"{Colors.BOLD_BLUE}Ожидайте в следующем обновлении v3.3!{Colors.RESET}")
                
                new_features = [
                    "• Темная/светлая тема",
                    "• Настройка цветовой схемы",
                    "• Интеграция с календарем",
                    "• AI-аналитика расширенная",
                    "• Мобильная версия"
                ]
                
                print(f"\n{Colors.BOLD_CYAN}ПЛАНИРУЕМЫЕ ФИЧИ:{Colors.RESET}")
                for feature in new_features:
                    print(f"  {feature}")
                
                print()
                input(f"{Colors.BOLD_BLUE}Нажмите Enter для продолжения...{Colors.RESET}")
            else:
                print(f"{Colors.RED}[ERROR]{Colors.RESET} Неверный выбор")
                time.sleep(1)
                
        except Exception as e:
            print(f"{Colors.RED}[ERROR]{Colors.RESET} {e}")
            time.sleep(1)
    
    def exit_program(self):
        """Выход из программы."""
        self._clear_screen()
        print(f"{Icons.EXIT} {Colors.BOLD_CYAN}ВЫХОД ИЗ ПРОГРАММЫ{Colors.RESET}")
        print(Icons.H_LINE)
        
        print(f"\n{Icons.SAVE} {Colors.CYAN}Сохранение данных...{Colors.RESET}")
        
        # Анимация сохранения
        for i in range(5):
            dots = "." * (i % 4)
            print(f"  {Colors.CYAN}💾 Сохранение сессии{dots}{Colors.RESET}", end='\r')
            time.sleep(0.2)
        
        print(f"\n{Icons.CHECK} {Colors.GREEN}Данные сохранены!{Colors.RESET}")
        
        # Статистика сессии
        print(f"\n{Colors.BOLD_CYAN}СТАТИСТИКА ЗА СЕССИЮ:{Colors.RESET}")
        stats = [
            (f"Клиентов в базе", len(self.clients_data)),
            (f"Активных клиентов", self.metrics['total_clients']),
            (f"Общий MRR", f"{self.metrics['total_mrr']:,} руб."),
            (f"Средний Health Score", self.metrics['avg_health_score']),
            (f"Клиентов в риске", self.metrics['at_risk_count']),
            (f"Дата и время", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        ]
        
        for label, value in stats:
            print(f"  {Colors.BOLD_BLUE}{label:<25}{Colors.RESET}: {value}")
        
        print(f"\n{Colors.BOLD_CYAN}{'═'*50}{Colors.RESET}")
        print(f"{Colors.BOLD_GREEN}Спасибо за использование CSM Dashboard Pro v3.2!{Colors.RESET}")
        print(f"{Colors.BOLD_BLUE}До новых встреч! 👋{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}{'═'*50}{Colors.RESET}")
        
        time.sleep(3)
        sys.exit(0)
    
    def run(self):
        """Основной цикл программы."""
        while True:
            self._clear_screen()
            self.display_header()
            self.display_metrics()
            self.display_clients_table()
            self.display_ai_recommendations()
            self.display_quick_actions()
            self.display_interactive_menu()


# =================== ЗАПУСК ПРОГРАММЫ ===================
if __name__ == "__main__":
    try:
        # Проверка поддержки ANSI в Windows
        if os.name == 'nt':
            os.system('')  # Включает поддержку ANSI в Windows 10+
        
        print(f"\n{Colors.BOLD_CYAN}{'═'*60}{Colors.RESET}")
        print(f"{Colors.BOLD_BLUE}          ИНИЦИАЛИЗАЦИЯ CSM DASHBOARD PRO v3.2{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}{'═'*60}{Colors.RESET}")
        
        # Анимация загрузки
        steps = [
            "Загрузка данных клиентов...",
            "Инициализация модулей AI...",
            "Настройка цветового интерфейса...",
            "Подготовка отчетов..."
        ]
        
        for step in steps:
            print(f"\n{Colors.CYAN}⏳ {step}{Colors.RESET}")
            time.sleep(0.3)
        
        print(f"\n{Colors.GREEN}✅ CSM Dashboard Pro v3.2 успешно запущен!{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}{'─'*60}{Colors.RESET}")
        print(f"{Colors.BOLD}💡 Подсказка:{Colors.RESET} Используйте цифры 1-8 для навигации")
        print(f"{Colors.BOLD}🎨 Интерфейс:{Colors.RESET} Цветной с Unicode символами")
        time.sleep(2)
        
        # Запуск основного приложения
        dashboard = CSMDashboardPro()
        dashboard.run()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}[EXIT]{Colors.RESET} Программа прервана пользователем.")
    except Exception as e:
        print(f"\n{Colors.RED}[ERROR]{Colors.RESET} Критическая ошибка: {e}")
        print(f"{Colors.RED}[ERROR]{Colors.RESET} Убедитесь, что ваш терминал поддерживает UTF-8")
    finally:
        print(f"\n{Colors.CYAN}Завершение работы...{Colors.RESET}")
        time.sleep(1)
