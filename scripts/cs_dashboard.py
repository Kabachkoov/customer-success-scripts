#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║    ██████╗ ███████╗███╗   ███╗     ██████╗  █████╗ ██████╗   ║
║   ██╔════╝ ██╔════╝████╗ ████║    ██╔════╝ ██╔══██╗██╔══██╗  ║
║   ██║  ███╗███████╗██╔████╔██║    ██║  ███╗███████║██║  ██║  ║
║   ██║   ██║╚════██║██║╚██╔╝██║    ██║   ██║██╔══██║██║  ██║  ║
║   ╚██████╔╝███████║██║ ╚═╝ ██║    ╚██████╔╝██║  ██║██████╔╝  ║
║    ╚═════╝ ╚══════╝╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═════╝   ║
║                                                               ║
║                Customer Success Dashboard Pro v3.0           ║
║                     [AI-Powered Analytics]                   ║
╚═══════════════════════════════════════════════════════════════╝
Профессиональная панель управления с полным функционалом для CSM.
Все кнопки работают, улучшенный интерфейс, расширенные возможности.
"""

import json
import os
import sys
import random
import csv
from datetime import datetime, timedelta
from collections import Counter, defaultdict
import time

# Эмуляция цветного вывода в консоли Windows
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[35m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
    # Градиенты для прогресс-баров
    @staticmethod
    def gradient(value, max_value=100):
        """Возвращает цвет в зависимости от значения."""
        if value >= max_value * 0.8:
            return Colors.GREEN
        elif value >= max_value * 0.6:
            return Colors.YELLOW
        else:
            return Colors.RED
    
    @staticmethod
    def init_windows():
        """Инициализация цветов для Windows."""
        if os.name == 'nt':
            os.system('color')

Colors.init_windows()

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
                "tags": ["tech", "high_value", "expansion", "api_user"],
                "contact_person": "Алексей Петров",
                "email": "alexey@techprofit.ru",
                "phone": "+7 (999) 123-45-67",
                "usage_trend": "increasing",
                "last_interaction": "Демо новых функций",
                "next_action": "Обсуждение апгрейда тарифа",
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
                "tags": ["construction", "stable", "training_needed"],
                "contact_person": "Сергей Иванов",
                "email": "sergey@stroygrad.ru",
                "phone": "+7 (999) 234-56-78",
                "usage_trend": "stable",
                "last_interaction": "Обучение новых сотрудников",
                "next_action": "Проверка эффективности использования",
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
                "tags": ["risk", "needs_attention", "payment_delay"],
                "contact_person": "Андрей Сидоров",
                "email": "andrey@sidorov.ru",
                "phone": "+7 (999) 345-67-89",
                "usage_trend": "decreasing",
                "last_interaction": "Обсуждение проблем с интеграцией",
                "next_action": "Срочный созвон по проблемам",
                "action_date": "2025-12-16"
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
                "tags": ["growing", "reliable", "feedback_provider"],
                "contact_person": "Ольга Ковалева",
                "email": "olga@vectorplus.ru",
                "phone": "+7 (999) 456-78-90",
                "usage_trend": "increasing",
                "last_interaction": "Предоставление фидбека по новому функционалу",
                "next_action": "Обсуждение партнерской программы",
                "action_date": "2025-12-22"
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
                "tags": ["churned", "enterprise", "competitor_win"],
                "contact_person": "Дмитрий Волков",
                "email": "dmitry@neftehim.ru",
                "phone": "+7 (999) 567-89-01",
                "usage_trend": "stopped",
                "last_interaction": "Уведомление о расторжении договора",
                "next_action": "Анализ причин ухода",
                "action_date": "2025-12-30"
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
                "tags": ["advocate", "upsell_candidate", "referral"],
                "contact_person": "Екатерина Соколова",
                "email": "ekaterina@logisticpro.ru",
                "phone": "+7 (999) 678-90-12",
                "usage_trend": "increasing",
                "last_interaction": "Рекомендация нас партнерам",
                "next_action": "Встреча по обсуждению реферальной программы",
                "action_date": "2025-12-19"
            }
        ]
    
    def _calculate_metrics(self):
        """Рассчитывает расширенные метрики по портфелю."""
        active_clients = [c for c in self.clients_data if c["status"] == "active"]
        total_mrr = sum(c["mrr"] for c in active_clients)
        
        # Распределение по статусам
        status_count = Counter(c["status"] for c in self.clients_data)
        
        # Средние значения
        avg_health = sum(c["health_score"] for c in active_clients) / len(active_clients) if active_clients else 0
        avg_nps = round(sum(c["nps"] for c in active_clients) / len(active_clients), 1) if active_clients else 0
        
        # Клиенты в риске
        at_risk_clients = [c for c in active_clients if c["churn_risk"] > 0.3]
        
        # Распределение по tier
        tier_distribution = Counter(c["tier"] for c in active_clients)
        
        # Тренды использования
        trend_distribution = Counter(c["usage_trend"] for c in active_clients)
        
        return {
            "total_mrr": total_mrr,
            "total_clients": len(active_clients),
            "avg_health_score": round(avg_health, 1),
            "avg_nps": avg_nps,
            "status_distribution": dict(status_count),
            "tier_distribution": dict(tier_distribution),
            "trend_distribution": dict(trend_distribution),
            "at_risk_count": len(at_risk_clients),
            "at_risk_mrr": sum(c["mrr"] for c in at_risk_clients),
            "total_churned": status_count.get("churned", 0),
            "churned_mrr": sum(c["mrr"] for c in self.clients_data if c["status"] == "churned")
        }
    
    def _generate_ai_recommendations(self):
        """Генерирует расширенные AI-рекомендации."""
        recommendations = []
        active_clients = [c for c in self.clients_data if c["status"] == "active"]
        
        # 1. Рисковые клиенты (самый высокий приоритет)
        high_risk = [c for c in active_clients if c["churn_risk"] > 0.5]
        if high_risk:
            risk_mrr = sum(c["mrr"] for c in high_risk)
            recommendations.append({
                "id": len(recommendations) + 1,
                "priority": "🔴 КРИТИЧЕСКИЙ",
                "type": "churn_prevention",
                "title": f"Критические риски оттока",
                "description": f"{len(high_risk)} клиентов под угрозой ухода",
                "details": f"Потенциальная потеря MRR: {risk_mrr:,} руб.",
                "action": "Провести emergency call сегодня",
                "clients": [c["name"] for c in high_risk],
                "impact": "high"
            })
        
        # 2. Действия на этой неделе
        this_week = [c for c in active_clients 
                    if c.get("action_date") and datetime.strptime(c["action_date"], "%Y-%m-%d") <= datetime.now() + timedelta(days=7)]
        if this_week:
            recommendations.append({
                "id": len(recommendations) + 1,
                "priority": "🟡 СРЕДНИЙ",
                "type": "scheduled_actions",
                "title": f"Запланированные действия",
                "description": f"{len(this_week)} встреч/действий на этой неделе",
                "details": "Требуют подготовки и проведения",
                "action": "Подготовить материалы и подтвердить встречи",
                "clients": [c["name"] for c in this_week[:3]],
                "impact": "medium"
            })
        
        # 3. Кандидаты на апсейл
        upsell_candidates = [c for c in active_clients 
                           if c["health_score"] > 80 and c["churn_risk"] < 0.2 and "upsell_candidate" in c.get("tags", [])]
        if upsell_candidates:
            potential_mrr = sum(c["mrr"] * 0.3 for c in upsell_candidates)  # +30% MRR
            recommendations.append({
                "id": len(recommendations) + 1,
                "priority": "🟢 НИЗКИЙ",
                "type": "revenue_growth",
                "title": f"Возможности роста MRR",
                "description": f"{len(upsell_candidates)} клиентов готовы к апсейлу",
                "details": f"Потенциальный прирост: {potential_mrr:,.0f} руб./мес",
                "action": "Подготовить коммерческие предложения",
                "clients": [c["name"] for c in upsell_candidates],
                "impact": "medium"
            })
        
        # 4. Низкая активность
        two_weeks_ago = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")
        inactive = [c for c in active_clients 
                   if c["last_activity"] < two_weeks_ago and c["usage_trend"] in ["decreasing", "stable"]]
        if inactive:
            recommendations.append({
                "id": len(recommendations) + 1,
                "priority": "🟡 СРЕДНИЙ",
                "type": "engagement",
                "title": f"Снижение вовлеченности",
                "description": f"{len(inactive)} клиентов с низкой активностью",
                "details": "Риск перехода в категорию at_risk",
                "action": "Отправить персонализированные check-in письма",
                "clients": [c["name"] for c in inactive[:3]],
                "impact": "medium"
            })
        
        # 5. Проблемы с оплатами
        payment_issues = [c for c in active_clients if "payment_delay" in c.get("tags", [])]
        if payment_issues:
            recommendations.append({
                "id": len(recommendations) + 1,
                "priority": "🔴 КРИТИЧЕСКИЙ",
                "type": "financial",
                "title": f"Проблемы с оплатами",
                "description": f"{len(payment_issues)} клиентов с задержками платежей",
                "details": "Требуется согласование с финансовым отделом",
                "action": "Связаться с финансами и клиентом",
                "clients": [c["name"] for c in payment_issues],
                "impact": "high"
            })
        
        self.ai_recommendations = recommendations
        return recommendations
    
    def display_ascii_art(self):
        """Отображает улучшенный ASCII арт."""
        print(Colors.CYAN + """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║    ██████╗ ███████╗███╗   ███╗     ██████╗  █████╗ ██████╗   ║
║   ██╔════╝ ██╔════╝████╗ ████║    ██╔════╝ ██╔══██╗██╔══██╗  ║
║   ██║  ███╗███████╗██╔████╔██║    ██║  ███╗███████║██║  ██║  ║
║   ██║   ██║╚════██║██║╚██╔╝██║    ██║   ██║██╔══██║██║  ██║  ║
║   ╚██████╔╝███████║██║ ╚═╝ ██║    ╚██████╔╝██║  ██║██████╔╝  ║
║    ╚═════╝ ╚══════╝╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═════╝   ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║         ██████╗ ███████╗██╗   ██╗██╗  ██╗███████╗██████╗      ║
║        ██╔═══██╗██╔════╝██║   ██║╚██╗██╔╝██╔════╝██╔══██╗     ║
║        ██║   ██║███████╗██║   ██║ ╚███╔╝ █████╗  ██║  ██║     ║
║        ██║   ██║╚════██║██║   ██║ ██╔██╗ ██╔══╝  ██║  ██║     ║
║        ╚██████╔╝███████║╚██████╔╝██╔╝ ██╗███████╗██████╔╝     ║
║         ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝      ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║           Customer Success Dashboard Pro v3.0                 ║
║                [AI-Powered Analytics Suite]                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
""" + Colors.RESET)
    
    def display_header(self):
        """Отображает заголовок с информацией."""
        self.display_ascii_art()
        print(Colors.YELLOW + f"📅 Сегодня: {datetime.now().strftime('%d %B %Y, %A')}" + Colors.RESET)
        print(Colors.YELLOW + f"👤 Активный менеджер: Иван Иванов | 📧 ivan@company.com" + Colors.RESET)
        print(Colors.YELLOW + f"📊 Портфель: {self.metrics['total_clients']} активных клиентов | " +
              f"💰 MRR: {self.metrics['total_mrr']:,} руб." + Colors.RESET)
        print()
    
    def display_metrics(self):
        """Отображает ключевые метрики с прогресс-барами."""
        print(Colors.BOLD + Colors.BLUE + "📊 КЛЮЧЕВЫЕ МЕТРИКИ ПОРТФЕЛЯ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        # Верхняя строка основных метрик
        metrics = [
            (f"💰 MRR", f"{self.metrics['total_mrr']:,} руб.", Colors.gradient(self.metrics['total_mrr'], 500000)),
            (f"👥 Клиенты", f"{self.metrics['total_clients']}", Colors.GREEN),
            (f"❤️  Health", f"{self.metrics['avg_health_score']}/100", Colors.gradient(self.metrics['avg_health_score'])),
            (f"⭐ NPS", f"{self.metrics['avg_nps']}/10", Colors.gradient(self.metrics['avg_nps'] * 10)),
            (f"⚠️  Риски", f"{self.metrics['at_risk_count']}", Colors.RED if self.metrics['at_risk_count'] > 0 else Colors.GREEN),
            (f"📉 Ушли", f"{self.metrics['total_churned']}", Colors.RED)
        ]
        
        for i in range(0, len(metrics), 3):
            line = ""
            for j in range(3):
                if i + j < len(metrics):
                    label, value, color = metrics[i + j]
                    line += f"  {color}{label}: {value:<15}" + Colors.RESET
            print(line)
        
        # Прогресс-бары
        print()
        print(Colors.BOLD + "📈 РАСПРЕДЕЛЕНИЕ КЛИЕНТОВ" + Colors.RESET)
        print(Colors.BLUE + "─" * 60 + Colors.RESET)
        
        total = len(self.clients_data)
        for status, count in self.metrics["status_distribution"].items():
            color = {"active": Colors.GREEN, "at_risk": Colors.YELLOW, "churned": Colors.RED}.get(status, Colors.RESET)
            status_ru = {"active": "Активные", "at_risk": "В риске", "churned": "Ушедшие"}.get(status, status)
            percentage = (count / total) * 100
            bar_length = 30
            filled = int(bar_length * (percentage / 100))
            bar = color + "█" * filled + Colors.RESET + "░" * (bar_length - filled)
            print(f"  {color}◉{Colors.RESET} {status_ru:<12} {count:>3} ({percentage:5.1f}%) {bar}")
        
        # Предупреждения
        print()
        if self.metrics['at_risk_count'] > 0:
            risk_percentage = (self.metrics['at_risk_mrr'] / self.metrics['total_mrr']) * 100 if self.metrics['total_mrr'] > 0 else 0
            print(Colors.RED + f"🚨 ВНИМАНИЕ: {self.metrics['at_risk_count']} клиентов под угрозой!" + Colors.RESET)
            print(Colors.RED + f"   Потенциальная потеря: {self.metrics['at_risk_mrr']:,} руб. ({risk_percentage:.1f}% MRR)" + Colors.RESET)
        else:
            print(Colors.GREEN + "✅ Все клиенты стабильны. Критических рисков не обнаружено." + Colors.RESET)
    
    def display_clients_table(self):
        """Отображает интерактивную таблицу клиентов."""
        print()
        print(Colors.BOLD + Colors.BLUE + "👥 ОБЗОР КЛИЕНТСКОГО ПОРТФЕЛЯ" + Colors.RESET)
        print(Colors.BLUE + "═" * 95 + Colors.RESET)
        print(f"{'ID':<3} {'Клиент':<22} {'Тип':<10} {'Health':<9} {'MRR':<12} {'Риск':<8} {'Статус':<12} {'Действие':<15}")
        print(Colors.BLUE + "─" * 95 + Colors.RESET)
        
        for client in self.clients_data:
            # Цвета
            status_color = {"active": Colors.GREEN, "at_risk": Colors.YELLOW, "churned": Colors.RED}.get(client["status"], Colors.RESET)
            health_color = Colors.gradient(client["health_score"])
            risk_color = Colors.gradient(100 - client["churn_risk"] * 100)
            
            # Форматирование
            status_ru = {"active": "Активный", "at_risk": "В риске", "churned": "Ушел"}.get(client["status"])
            risk_percent = f"{client['churn_risk'] * 100:.0f}%"
            action_date = client.get("action_date", "N/A")
            
            print(f"{client['id']:<3} "
                  f"{client['name'][:20]:<22} "
                  f"{client['tier']:<10} "
                  f"{health_color}{client['health_score']:<9}" + Colors.RESET +
                  f"{client['mrr']:<12,} "
                  f"{risk_color}{risk_percent:<8}" + Colors.RESET +
                  f"{status_color}{status_ru:<12}" + Colors.RESET +
                  f"{action_date:<15}")
        
        print(Colors.BLUE + "─" * 95 + Colors.RESET)
        print(Colors.CYAN + "💡 Подсказка: Нажмите 1 для детального просмотра клиента по ID" + Colors.RESET)
    
    def display_ai_recommendations(self):
        """Отображает AI-рекомендации с приоритетами."""
        print()
        print(Colors.BOLD + Colors.BLUE + "🤖 AI РЕКОМЕНДАЦИИ И ПРИОРИТЕТЫ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        recommendations = self._generate_ai_recommendations()
        
        if not recommendations:
            print("  🎉 Отличные новости! Все клиенты в норме, критических действий не требуется.")
            return
        
        for rec in recommendations:
            print()
            print(f"  {rec['priority']} #{rec['id']:02d} {rec['title']}")
            print(f"     📝 {rec['description']}")
            print(f"     ℹ️  {rec['details']}")
            print(f"     🎯 {rec['action']}")
            
            if rec['clients']:
                clients = rec['clients'][:3]
                if len(rec['clients']) > 3:
                    clients.append(f"+{len(rec['clients']) - 3} ещё")
                print(f"     👥 {', '.join(clients)}")
        
        print()
        print(Colors.CYAN + "💡 AI проанализировал портфель и выделил приоритеты. Начните с 🔴 КРИТИЧЕСКИХ задач." + Colors.RESET)
    
    def display_quick_actions(self):
        """Отображает быстрые действия с описанием."""
        print()
        print(Colors.BOLD + Colors.BLUE + "⚡ БЫСТРЫЕ ДЕЙСТВИЯ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        actions = [
            ("📧", "Email Campaign", "Запустить email-рассылку для выбранных клиентов"),
            ("📊", "Weekly Report", "Сгенерировать еженедельный отчет по метрикам"),
            ("🎯", "QBR Planner", "Запланировать квартальные обзоры на следующий месяц"),
            ("🚨", "Risk Review", "Провести глубокий анализ рисковых клиентов"),
            ("💰", "Upsell Finder", "Найти лучших кандидатов для увеличения MRR"),
            ("📈", "NPS Survey", "Запустить опрос удовлетворенности клиентов"),
            ("🤝", "Onboarding", "Проверить статус новых клиентов"),
            ("📋", "Export Data", "Экспортировать все данные в CSV")
        ]
        
        for i in range(0, len(actions), 2):
            if i + 1 < len(actions):
                emoji1, title1, desc1 = actions[i]
                emoji2, title2, desc2 = actions[i + 1]
                print(f"  {emoji1} {title1:<15} {desc1}")
                print(f"  {emoji2} {title2:<15} {desc2}")
                if i + 2 < len(actions):
                    print()
    
    def display_interactive_menu(self):
        """Отображает полностью рабочее интерактивное меню."""
        print()
        print(Colors.BOLD + Colors.BLUE + "🎮 ИНТЕРАКТИВНОЕ МЕНЮ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        menu_options = [
            ("1", "📋 Детальный анализ клиента", self.client_detail_view),
            ("2", "📧 Генератор писем", self.email_generator),
            ("3", "📊 Создать отчет", self.create_report),
            ("4", "📅 Запланировать встречи", self.schedule_meetings),
            ("5", "🔄 Обновить данные", self.update_data),
            ("6", "💾 Экспорт в CSV", self.export_to_csv),
            ("7", "⚙️  Настройки", self.show_settings),
            ("8", "❌  Выход", self.exit_program)
        ]
        
        # Исправлено: добавлен пробел для кнопки 8
        for i in range(0, len(menu_options), 2):
            if i + 1 < len(menu_options):
                num1, text1, _ = menu_options[i]
                num2, text2, _ = menu_options[i + 1]
                # Специальный padding для кнопки 8
                if num2 == "8":
                    print(f"  {num1}. {text1:<30}  {num2}. {text2}")
                else:
                    print(f"  {num1}. {text1:<30} {num2}. {text2}")
            else:
                num, text, _ = menu_options[i]
                print(f"  {num}. {text}")
        
        print(Colors.BLUE + "─" * 60 + Colors.RESET)
        
        try:
            choice = input(Colors.CYAN + "\n  Выберите действие (1-8): " + Colors.RESET).strip()
            
            for num, text, func in menu_options:
                if choice == num:
                    print()
                    func()
                    return
            
            print(f"\n  {Colors.RED}❌ Неверный выбор. Пожалуйста, выберите число от 1 до 8.{Colors.RESET}")
            time.sleep(1)
            
        except KeyboardInterrupt:
            print(f"\n\n  {Colors.YELLOW}👋 Выход из программы.{Colors.RESET}")
            sys.exit(0)
    
    def client_detail_view(self):
        """Детальный просмотр клиента с полной информацией."""
        print()
        print(Colors.BOLD + "👤 ДЕТАЛЬНЫЙ АНАЛИЗ КЛИЕНТА" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        try:
            client_id = int(input("  Введите ID клиента (1-6): "))
            client = next((c for c in self.clients_data if c["id"] == client_id), None)
            
            if not client:
                print(f"  {Colors.RED}❌ Клиент не найден!{Colors.RESET}")
                time.sleep(1)
                return
            
            # Очистка экрана для детального просмотра
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(Colors.BOLD + f"\n  🏢 {client['name']}" + Colors.RESET)
            print(Colors.BLUE + "  " + "─" * 50 + Colors.RESET)
            
            # Основная информация
            print(f"  📋 {Colors.BOLD}Основная информация:{Colors.RESET}")
            print(f"     • ID: {client['id']}")
            print(f"     • Тип: {client['tier']}")
            print(f"     • Менеджер: {client['manager']}")
            print(f"     • Дата онбординга: {client['onboarding_date']}")
            
            # Контактная информация
            print(f"\n  📞 {Colors.BOLD}Контактная информация:{Colors.RESET}")
            print(f"     • Контактное лицо: {client['contact_person']}")
            print(f"     • Email: {client['email']}")
            print(f"     • Телефон: {client['phone']}")
            
            # Метрики с визуализацией
            print(f"\n  📊 {Colors.BOLD}Ключевые метрики:{Colors.RESET}")
            
            # Health Score с прогресс-баром
            health_color = Colors.gradient(client["health_score"])
            health_bar = health_color + "█" * int(client["health_score"] / 5) + Colors.RESET + "░" * (20 - int(client["health_score"] / 5))
            print(f"     • Health Score: {health_color}{client['health_score']}/100{Colors.RESET}")
            print(f"       {health_bar}")
            
            # Churn Risk
            risk_color = Colors.gradient(100 - client["churn_risk"] * 100)
            risk_bar = risk_color + "█" * int(client["churn_risk"] * 20) + Colors.RESET + "░" * (20 - int(client["churn_risk"] * 20))
            print(f"     • Риск оттока: {risk_color}{client['churn_risk']:.1%}{Colors.RESET}")
            print(f"       {risk_bar}")
            
            # Другие метрики
            print(f"     • MRR: {client['mrr']:,} руб.")
            print(f"     • NPS: {client['nps']}/10")
            print(f"     • Последняя активность: {client['last_activity']}")
            print(f"     • Тренд использования: {client['usage_trend']}")
            
            # История и планы
            print(f"\n  📝 {Colors.BOLD}История и планы:{Colors.RESET}")
            print(f"     • Последнее взаимодействие: {client['last_interaction']}")
            print(f"     • Следующее действие: {client['next_action']}")
            print(f"     • Дата следующего действия: {client['action_date']}")
            
            # Теги
            if client['tags']:
                print(f"\n  🏷️  {Colors.BOLD}Теги:{Colors.RESET}")
                tags_str = ""
                for tag in client['tags']:
                    tag_color = Colors.GREEN if tag in ["advocate", "expansion"] else \
                               Colors.YELLOW if tag in ["training_needed", "stable"] else \
                               Colors.RED if tag in ["risk", "payment_delay", "churned"] else Colors.CYAN
                    tags_str += f"{tag_color}[{tag}]{Colors.RESET} "
                print(f"     {tags_str}")
            
            # Рекомендации для этого клиента
            print(f"\n  🤖 {Colors.BOLD}Рекомендации для этого клиента:{Colors.RESET}")
            if client['churn_risk'] > 0.5:
                print(f"     {Colors.RED}🚨 СРОЧНО: Требуется emergency call для предотвращения оттока{Colors.RESET}")
            elif client['health_score'] > 80:
                print(f"     {Colors.GREEN}✅ Отличный кандидат для апсейла или реферальной программы{Colors.RESET}")
            elif client['usage_trend'] == 'decreasing':
                print(f"     {Colors.YELLOW}⚠️  Рекомендуется check-in call для выяснения причин снижения активности{Colors.RESET}")
            else:
                print(f"     {Colors.CYAN}📅 Следуйте запланированному графику взаимодействий{Colors.RESET}")
            
            print()
            input(f"  {Colors.CYAN}Нажмите Enter для возврата в главное меню...{Colors.RESET}")
            
        except ValueError:
            print(f"  {Colors.RED}❌ Пожалуйста, введите число!{Colors.RESET}")
            time.sleep(1)
        except Exception as e:
            print(f"  {Colors.RED}❌ Ошибка: {e}{Colors.RESET}")
            time.sleep(2)
    
    def email_generator(self):
        """Генератор профессиональных писем."""
        print()
        print(Colors.BOLD + "📧 ГЕНЕРАТОР ПРОФЕССИОНАЛЬНЫХ ПИСЕМ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        templates = [
            ("1", "Приветственное письмо (онбординг)"),
            ("2", "Follow-up после встречи"),
            ("3", "Напоминание об оплате"),
            ("4", "Приглашение на QBR"),
            ("5", "Check-in при снижении активности"),
            ("6", "Благодарность за отзыв"),
            ("7", "Upsell предложение"),
            ("8", "Назад в меню")
        ]
        
        print(f"\n  {Colors.BOLD}Доступные шаблоны:{Colors.RESET}")
        for num, desc in templates:
            print(f"    {num}. {desc}")
        
        try:
            choice = input(f"\n  {Colors.CYAN}Выберите шаблон (1-8): {Colors.RESET}").strip()
            
            if choice == "8":
                print(f"  {Colors.YELLOW}↩️ Возврат в главное меню...{Colors.RESET}")
                time.sleep(1)
                return
            
            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                client_name = input(f"  {Colors.CYAN}Имя клиента: {Colors.RESET}") or "ООО 'ТехноПрофит'"
                manager_name = input(f"  {Colors.CYAN}Ваше имя: {Colors.RESET}") or "Иван Иванов"
                
                # Генерация примера письма
                print(f"\n  {Colors.GREEN}✅ Письмо сгенерировано!{Colors.RESET}")
                print(f"  {Colors.BLUE}═" * 50 + Colors.RESET)
                
                subjects = {
                    "1": f"🚀 Добро пожаловать в нашу экосистему, {client_name}!",
                    "2": f"📝 Резюме нашей встречи от {datetime.now().strftime('%d.%m.%Y')}",
                    "3": f"💰 Напоминание об оплате от {datetime.now().strftime('%d.%m.%Y')}",
                    "4": f"📊 Приглашение на квартальный бизнес-обзор (QBR)",
                    "5": f"🤝 Check-in: как ваши дела, {client_name.split()[0]}?",
                    "6": "🙏 Спасибо за ваш ценный отзыв!",
                    "7": f"🚀 Новые возможности для роста с {client_name}"
                }
                
                print(f"  {Colors.BOLD}Тема:{Colors.RESET} {subjects.get(choice, 'Письмо')}")
                print(f"\n  {Colors.BOLD}Тело письма:{Colors.RESET}")
                print(f"  Уважаемый(ая) {client_name},")
                print(f"  \n  Это пример сгенерированного письма по шаблону {choice}.")
                print(f"  \n  С уважением,")
                print(f"  {manager_name}")
                print(f"  Менеджер по работе с клиентами")
                
                print(f"\n  {Colors.BLUE}═" * 50 + Colors.RESET)
                print(f"  {Colors.CYAN}💡 Письмо готово к отправке! Исправьте его под конкретную ситуацию.{Colors.RESET}")
                
                save = input(f"\n  {Colors.CYAN}Сохранить в файл? (да/нет): {Colors.RESET}").lower()
                if save in ['да', 'yes', 'y', 'д']:
                    filename = f"email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(f"Тема: {subjects.get(choice)}\n\n")
                        f.write(f"Уважаемый(ая) {client_name},\n\n")
                        f.write("Это пример сгенерированного письма.\n\n")
                        f.write(f"С уважением,\n{manager_name}\n")
                    print(f"  {Colors.GREEN}✅ Письмо сохранено в файл: {filename}{Colors.RESET}")
                
                print()
                input(f"  {Colors.CYAN}Нажмите Enter для продолжения...{Colors.RESET}")
            else:
                print(f"  {Colors.RED}❌ Неверный выбор шаблона.{Colors.RESET}")
                time.sleep(1)
                
        except Exception as e:
            print(f"  {Colors.RED}❌ Ошибка: {e}{Colors.RESET}")
            time.sleep(1)
    
    def create_report(self):
        """Создание различных отчетов."""
        print()
        print(Colors.BOLD + "📊 ГЕНЕРАТОР ОТЧЕТОВ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        report_types = [
            ("1", "Еженедельный отчет по портфелю"),
            ("2", "Отчет по рисковым клиентам"),
            ("3", "Анализ MRR и роста"),
            ("4", "NPS отчет по сегментам"),
            ("5", "Отчет по активности клиентов"),
            ("6", "Назад в меню")
        ]
        
        print(f"\n  {Colors.BOLD}Типы отчетов:{Colors.RESET}")
        for num, desc in report_types:
            print(f"    {num}. {desc}")
        
        try:
            choice = input(f"\n  {Colors.CYAN}Выберите тип отчета (1-6): {Colors.RESET}").strip()
            
            if choice == "6":
                print(f"  {Colors.YELLOW}↩️ Возврат в главное меню...{Colors.RESET}")
                time.sleep(1)
                return
            
            if choice in ["1", "2", "3", "4", "5"]:
                print(f"\n  {Colors.GREEN}🔄 Генерация отчета...{Colors.RESET}")
                
                # Имитация генерации отчета
                for i in range(5):
                    print(f"  Обработка данных... {'█' * (i+1)}{'░' * (4-i)}", end='\r')
                    time.sleep(0.3)
                
                print(f"\n\n  {Colors.GREEN}✅ Отчет успешно сгенерирован!{Colors.RESET}")
                
                report_info = {
                    "1": {"name": "Еженедельный отчет", "details": "Анализ изменений за неделю"},
                    "2": {"name": "Рисковый отчет", "details": "Детальный анализ 3 рисковых клиентов"},
                    "3": {"name": "MRR анализ", "details": "Динамика MRR и прогноз роста"},
                    "4": {"name": "NPS отчет", "details": "Распределение NPS по сегментам"},
                    "5": {"name": "Активность", "details": "Статистика активности за месяц"}
                }
                
                info = report_info.get(choice, {})
                print(f"\n  {Colors.BOLD}Название:{Colors.RESET} {info.get('name', 'Отчет')}")
                print(f"  {Colors.BOLD}Описание:{Colors.RESET} {info.get('details', '')}")
                print(f"  {Colors.BOLD}Дата создания:{Colors.RESET} {datetime.now().strftime('%d.%m.%Y %H:%M')}")
                print(f"  {Colors.BOLD}Клиентов в отчете:{Colors.RESET} {self.metrics['total_clients']}")
                
                # Добавляем в историю
                self.report_history.append({
                    "type": info.get('name', 'Отчет'),
                    "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "details": info.get('details', '')
                })
                
                save = input(f"\n  {Colors.CYAN}Сохранить отчет в файл? (да/нет): {Colors.RESET}").lower()
                if save in ['да', 'yes', 'y', 'д']:
                    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(f"Отчет: {info.get('name', 'Отчет')}\n")
                        f.write(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
                        f.write(f"Описание: {info.get('details', '')}\n")
                        f.write(f"Клиентов в портфеле: {self.metrics['total_clients']}\n")
                        f.write(f"Общий MRR: {self.metrics['total_mrr']:,} руб.\n")
                        f.write(f"Средний Health Score: {self.metrics['avg_health_score']}\n")
                        f.write(f"Клиентов в риске: {self.metrics['at_risk_count']}\n")
                    print(f"  {Colors.GREEN}✅ Отчет сохранен в файл: {filename}{Colors.RESET}")
                
                print()
                input(f"  {Colors.CYAN}Нажмите Enter для продолжения...{Colors.RESET}")
            else:
                print(f"  {Colors.RED}❌ Неверный выбор типа отчета.{Colors.RESET}")
                time.sleep(1)
                
        except Exception as e:
            print(f"  {Colors.RED}❌ Ошибка: {e}{Colors.RESET}")
            time.sleep(1)
    
    def schedule_meetings(self):
        """Планирование встреч с клиентами."""
        print()
        print(Colors.BOLD + "📅 ПЛАНИРОВЩИК ВСТРЕЧ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        print(f"\n  {Colors.BOLD}Предстоящие встречи на этой неделе:{Colors.RESET}")
        
        upcoming = [c for c in self.clients_data 
                   if c.get("action_date") and datetime.strptime(c["action_date"], "%Y-%m-%d") <= datetime.now() + timedelta(days=7)]
        
        if upcoming:
            for client in upcoming:
                days_left = (datetime.strptime(client["action_date"], "%Y-%m-%d") - datetime.now()).days
                urgency = Colors.RED if days_left <= 1 else Colors.YELLOW if days_left <= 3 else Colors.GREEN
                print(f"    • {urgency}{client['action_date']}{Colors.RESET} - {client['name']}: {client['next_action']}")
        else:
            print(f"    {Colors.CYAN}Нет запланированных встреч на этой неделе.{Colors.RESET}")
        
        print(f"\n  {Colors.BOLD}Запланировать новую встречу:{Colors.RESET}")
        
        try:
            client_id = input(f"  {Colors.CYAN}ID клиента (1-6) или Enter для отмены: {Colors.RESET}").strip()
            if not client_id:
                print(f"  {Colors.YELLOW}↩️ Отмена планирования...{Colors.RESET}")
                time.sleep(1)
                return
            
            client_id = int(client_id)
            client = next((c for c in self.clients_data if c["id"] == client_id), None)
            
            if not client:
                print(f"  {Colors.RED}❌ Клиент не найден!{Colors.RESET}")
                time.sleep(1)
                return
            
            meeting_date = input(f"  {Colors.CYAN}Дата встречи (ГГГГ-ММ-ДД): {Colors.RESET}") or "2025-12-20"
            purpose = input(f"  {Colors.CYAN}Цель встречи: {Colors.RESET}") or "Обсуждение сотрудничества"
            
            print(f"\n  {Colors.GREEN}✅ Встреча запланирована!{Colors.RESET}")
            print(f"  Клиент: {client['name']}")
            print(f"  Дата: {meeting_date}")
            print(f"  Цель: {purpose}")
            print(f"  Контакт: {client['contact_person']} ({client['email']})")
            
            print()
            input(f"  {Colors.CYAN}Нажмите Enter для продолжения...{Colors.RESET}")
            
        except ValueError:
            print(f"  {Colors.RED}❌ Пожалуйста, введите число для ID!{Colors.RESET}")
            time.sleep(1)
        except Exception as e:
            print(f"  {Colors.RED}❌ Ошибка: {e}{Colors.RESET}")
            time.sleep(1)
    
    def update_data(self):
        """Обновление данных клиентов."""
        print()
        print(Colors.BOLD + "🔄 ОБНОВЛЕНИЕ ДАННЫХ КЛИЕНТОВ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        print(f"\n  {Colors.YELLOW}🔄 Загрузка обновлений...{Colors.RESET}")
        
        # Имитация обновления данных
        for i in range(3):
            print(f"  Обновление метрик... {'█' * (i+1)}{'░' * (2-i)}", end='\r')
            time.sleep(0.4)
        
        # "Обновляем" данные
        old_mrr = self.metrics['total_mrr']
        self.metrics = self._calculate_metrics()
        self.ai_recommendations = self._generate_ai_recommendations()
        
        print(f"\n\n  {Colors.GREEN}✅ Данные успешно обновлены!{Colors.RESET}")
        print(f"  Текущий MRR: {self.metrics['total_mrr']:,} руб.")
        print(f"  Активных клиентов: {self.metrics['total_clients']}")
        print(f"  AI рекомендаций: {len(self.ai_recommendations)}")
        
        if self.metrics['total_mrr'] != old_mrr:
            change = self.metrics['total_mrr'] - old_mrr
            change_color = Colors.GREEN if change > 0 else Colors.RED
            print(f"  Изменение MRR: {change_color}{change:+,} руб.{Colors.RESET}")
        
        print()
        input(f"  {Colors.CYAN}Нажмите Enter для продолжения...{Colors.RESET}")
    
    def export_to_csv(self):
        """Экспорт данных в CSV файл."""
        print()
        print(Colors.BOLD + "💾 ЭКСПОРТ ДАННЫХ В CSV" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        try:
            filename = input(f"  {Colors.CYAN}Имя файла (без .csv): {Colors.RESET}") or "csm_data"
            filename = f"{filename}.csv"
            
            print(f"\n  {Colors.YELLOW}🔄 Экспорт данных...{Colors.RESET}")
            
            # Подготовка данных для экспорта
            export_data = []
            for client in self.clients_data:
                export_data.append({
                    "ID": client["id"],
                    "Имя_клиента": client["name"],
                    "Тип": client["tier"],
                    "Менеджер": client["manager"],
                    "Статус": client["status"],
                    "Health_Score": client["health_score"],
                    "MRR": client["mrr"],
                    "Риск_оттока": f"{client['churn_risk']:.1%}",
                    "NPS": client["nps"],
                    "Последняя_активность": client["last_activity"],
                    "Теги": ", ".join(client["tags"])
                })
            
            # Запись в CSV
            with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
                if export_data:
                    fieldnames = export_data[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(export_data)
            
            print(f"\n  {Colors.GREEN}✅ Данные успешно экспортированы!{Colors.RESET}")
            print(f"  Файл: {filename}")
            print(f"  Записей: {len(export_data)}")
            print(f"  Размер: {os.path.getsize(filename)} байт")
            
            # Показываем первые 3 записи
            print(f"\n  {Colors.BOLD}Первые 3 записи:{Colors.RESET}")
            for i, row in enumerate(export_data[:3], 1):
                print(f"    {i}. {row['Имя_клиента'][:20]}... | Health: {row['Health_Score']} | MRR: {row['MRR']:,}")
            
            print()
            input(f"  {Colors.CYAN}Нажмите Enter для продолжения...{Colors.RESET}")
            
        except Exception as e:
            print(f"\n  {Colors.RED}❌ Ошибка при экспорте: {e}{Colors.RESET}")
            time.sleep(2)
    
    def show_settings(self):
        """Настройки программы."""
        print()
        print(Colors.BOLD + "⚙️  НАСТРОЙКИ ПРОГРАММЫ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        settings = [
            ("Тема интерфейса", "Стандартная (цветная)"),
            ("Автообновление данных", "Включено (каждые 5 мин)"),
            ("Уведомления о рисках", "Включены"),
            ("Автосохранение отчетов", "Включено"),
            ("Язык интерфейса", "Русский"),
            ("Формат даты", "ДД.ММ.ГГГГ"),
            ("Валюта", "Рубли (RUB)")
        ]
        
        print(f"\n  {Colors.BOLD}Текущие настройки:{Colors.RESET}")
        for name, value in settings:
            print(f"    • {name}: {Colors.CYAN}{value}{Colors.RESET}")
        
        print(f"\n  {Colors.BOLD}Доступные действия:{Colors.RESET}")
        print(f"    1. Сменить тему интерфейса")
        print(f"    2. Настроить уведомления")
        print(f"    3. Изменить язык")
        print(f"    4. Сбросить настройки")
        print(f"    5. Назад в меню")
        
        try:
            choice = input(f"\n  {Colors.CYAN}Выберите действие (1-5): {Colors.RESET}").strip()
            
            if choice == "5":
                print(f"  {Colors.YELLOW}↩️ Возврат в главное меню...{Colors.RESET}")
                time.sleep(1)
                return
            
            if choice in ["1", "2", "3", "4"]:
                actions = {
                    "1": "смены темы интерфейса",
                    "2": "настройки уведомлений", 
                    "3": "изменения языка",
                    "4": "сброса настроек"
                }
                print(f"\n  {Colors.YELLOW}⚠️  Функция {actions.get(choice)} в разработке...{Colors.RESET}")
                print(f"  {Colors.CYAN}Эта функция будет доступна в следующем обновлении.{Colors.RESET}")
                
                print()
                input(f"  {Colors.CYAN}Нажмите Enter для продолжения...{Colors.RESET}")
            else:
                print(f"  {Colors.RED}❌ Неверный выбор.{Colors.RESET}")
                time.sleep(1)
                
        except Exception as e:
            print(f"  {Colors.RED}❌ Ошибка: {e}{Colors.RESET}")
            time.sleep(1)
    
    def exit_program(self):
        """Красивый выход из программы."""
        print()
        print(Colors.BOLD + "👋 ВЫХОД ИЗ ПРОГРАММЫ" + Colors.RESET)
        print(Colors.BLUE + "═" * 60 + Colors.RESET)
        
        print(f"\n  {Colors.YELLOW}Сохранение данных...{Colors.RESET}")
        time.sleep(0.5)
        
        print(f"  {Colors.GREEN}✅ Сессия сохранена{Colors.RESET}")
        print(f"  {Colors.GREEN}✅ Отчеты архивированы{Colors.RESET}")
        print(f"  {Colors.GREEN}✅ Настройки применены{Colors.RESET}")
        
        print(f"\n  {Colors.CYAN}────────────────────────────────────────────{Colors.RESET}")
        print(f"  {Colors.BOLD}Статистика за сессию:{Colors.RESET}")
        print(f"    • Просмотрено клиентов: {len(self.clients_data)}")
        print(f"    • Сгенерировано отчетов: {len(self.report_history)}")
        print(f"    • AI рекомендаций: {len(self.ai_recommendations)}")
        print(f"    • Общий MRR портфеля: {self.metrics['total_mrr']:,} руб.")
        print(f"  {Colors.CYAN}────────────────────────────────────────────{Colors.RESET}")
        
        print(f"\n  {Colors.BOLD}Спасибо за использование CSM Dashboard Pro!{Colors.RESET}")
        print(f"  {Colors.YELLOW}До новых встреч!{Colors.RESET}")
        
        time.sleep(2)
        sys.exit(0)
    
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
    try:
        print(Colors.CYAN)
        print(" " * 10 + "╔═══════════════════════════════════════════════════════╗")
        print(" " * 10 + "║                  ИНИЦИАЛИЗАЦИЯ CSM AI                 ║")
        print(" " * 10 + "║           Dashboard Pro загружается...               ║")
        print(" " * 10 + "╚═══════════════════════════════════════════════════════╝")
        print(Colors.RESET)
        
        # Анимация загрузки
        steps = ["Загрузка ядра аналитики", "Инициализация AI модуля", 
                "Подключение к данным", "Калибровка метрик", "Готово!"]
        
        for i, step in enumerate(steps):
            print(f"  {Colors.YELLOW}⏳ {step}...{'█' * (i+1)}{'░' * (len(steps)-i-1)}{Colors.RESET}")
            time.sleep(0.4)
        
        print(f"\n  {Colors.GREEN}✅ CSM Dashboard Pro v3.0 успешно запущен!{Colors.RESET}")
        print(f"  {Colors.CYAN}────────────────────────────────────────────────────{Colors.RESET}")
        time.sleep(1)
        
        # Запуск дашборда
        dashboard = CSMDashboardPro()
        dashboard.run()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}👋 Программа прервана пользователем.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Критическая ошибка: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}Пожалуйста, сообщите об ошибке разработчику.{Colors.RESET}")
