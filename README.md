<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=1a6fb5&height=200&section=header&text=ITC%20Analytics&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=Аналитика%20соцсетей%20и%202GIS%20колледжа&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<br/>

[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.4-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://chartjs.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> **Веб-дашборд для мониторинга репутации Инновационного Технического Колледжа (ITC Almaty)**  
> в социальных сетях Instagram и на платформе 2GIS

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1000&color=1A6FB5&center=true&vCenter=true&multiline=true&width=600&height=80&lines=📊+Аналитика+Instagram+%26+2GIS;🏆+Сравнение+с+конкурентами;🚀+Рекомендации+по+улучшению" alt="Typing SVG" />

</div>

---

## 📋 О проекте

Административная панель аналитики колледжа **ITC (Инновационный Технический Колледж)** в социальных сетях. Система агрегирует данные из Instagram и 2GIS, визуализирует метрики и формирует рекомендации по улучшению цифрового присутствия.

> ⚠️ **Данные имитационные** — проект использует mock JSON, структура которого идентична реальным API-ответам от Instagram и 2GIS.

---

## ✨ Функциональность

<table>
<tr>
<td width="50%">

### 📸 Instagram
- 📈 Динамика роста подписчиков
- 🎯 Engagement Rate (ER%)
- 🗂️ Типы контента (Reels / Карусель / Фото)
- 🏅 Топ публикации по охвату
- 📅 Активность по дням недели

</td>
<td width="50%">

### 🗺️ 2GIS
- ⭐ Рейтинг и распределение оценок
- 📊 Динамика отзывов по месяцам
- 🏷️ Популярные темы в отзывах
- 💬 Примеры отзывов студентов

</td>
</tr>
<tr>
<td>

### 💬 Тональность
- ✅ Позитивные отзывы
- ❌ Негативные отзывы
- ➖ Нейтральные комментарии
- 📊 Сравнение IG vs 2GIS

</td>
<td>

### 🏆 Конкуренты + 🚀 Рекомендации
- Сравнение с 4 колледжами Алматы
- Радар-диаграмма по метрикам
- 7 приоритизированных рекомендаций
- Оценка усилий и ожидаемый эффект

</td>
</tr>
</table>

---

## 🗂️ Структура проекта

```
iitc_analytics/
│
├── 📁 analytics/                   # Основное Django-приложение
│   ├── 📁 data/
│   │   └── 📄 mock_data.json       # Имитационные данные (Instagram + 2GIS)
│   ├── 📁 templates/analytics/
│   │   └── 📄 dashboard.html       # Главный дашборд (all-in-one)
│   ├── 📄 views.py                 # Загрузка JSON → контекст → render
│   └── 📄 urls.py                  # Маршруты: / и /api/data/
│
├── 📁 iitc_analytics/              # Конфигурация Django
│   ├── 📄 settings.py
│   └── 📄 urls.py
│
└── 📄 manage.py
```

---

## ⚡ Быстрый старт

### 1. Клонирование

```bash
git clone https://github.com/your-username/iitc-analytics.git
cd iitc-analytics
```

### 2. Установка зависимостей

```bash
pip install django
```

### 3. Применение миграций

```bash
python manage.py migrate
```

### 4. Запуск сервера

```bash
python manage.py runserver
```

### 5. Открыть в браузере

```
http://127.0.0.1:8000/
```

> Также доступен REST-эндпоинт с сырыми данными:  
> `http://127.0.0.1:8000/api/data/`

---

## 📊 Дашборд — разделы

| # | Раздел | Описание |
|---|--------|----------|
| 1 | **Обзор** | 4 KPI-карточки: подписчики, рейтинг, ER%, позитив |
| 2 | **Instagram** | Рост, контент, топ-посты, частота публикаций |
| 3 | **2GIS** | Звёзды, динамика, теги, примеры отзывов |
| 4 | **Тональность** | Сентимент IG и 2GIS, примеры по вкладкам |
| 5 | **Конкуренты** | Bar + Radar Chart, сводная таблица |
| 6 | **Рекомендации** | 7 карточек с приоритетом и эффектом |

---

## 🛠️ Технологии

<div align="center">

| Слой | Технология |
|------|-----------|
| Backend | ![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django) ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| Frontend | ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) |
| Charts | ![Chart.js](https://img.shields.io/badge/-Chart.js-FF6384?style=flat-square&logo=chartdotjs&logoColor=white) |
| Data | ![JSON](https://img.shields.io/badge/-JSON-000000?style=flat-square&logo=json) |
| Fonts | Google Fonts: Raleway + Open Sans |

</div>

---

## 📡 Источники данных

| Платформа | Ссылка | Статус |
|-----------|--------|--------|
| Instagram | [@it_college_almaty](https://www.instagram.com/it_college_almaty/) | 🟡 Mock |
| 2GIS | [ITC на 2GIS](https://2gis.kz/almaty/firm/70000001040563276) | 🟡 Mock |

---

## 👤 Автор

<div align="center">

**Алтынбек Сұлтан**  
Студент · RPO6-24R

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)](https://github.com/your-username)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=1a6fb5&height=100&section=footer" width="100%"/>

**ITC Analytics** · Инновационный Технический Колледж, Алматы

</div>
