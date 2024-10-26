# Цели проекта

1. Реализация анализа эмоций комментариев 
2. Реализация анализа токсичности комментариев
3. Распознавание замаскированной ненормативной лексики (скрытых оскорбительных выражений) 
4. Парсинг комментариев с стрима Twitch / Youtube
5. Эмоциональный анализ видео-аудио стрима
6. Автоматизация взаимодействия с токсичными комментариями

# Видение проекта через 3 месяца (к январю 2025)
Сервис для анализа тональности и эмоционального контекста комментариев на стриминговых платформах Twitch и YouTube. Проект может автоматизировать взаимодействие с зрителями, помогая стримерам и музыкальным лейблам сохранять репутацию

# Задачи

## Data Scientist / ML-инженер
1. Разработка архитектуры для анализа комментариев и видео/аудио стрима. Определение API взаимодействия составных частей
2. Обучение модели для анализа эмоций комментариев на основе текстовых данных с различных стримов.
3. Настройка алгоритмов анализа токсичности для классификации негативных комментариев.
4. Разработка распознавания замаскированной ненормативной лексики с учетом символов-заглушек (@, *, % и т.п.).
5. Видео-аудио анализ эмоционального фона стрима
6. Подготовка (предобработка входных данных) для тестирования и обучения модели

## Backend-разработчик
7. Реализация на Twitch/Youtube реагирования на токсичные комментарии: временная блокировка, отправка предупреждений и удаление комментариев.
8. Сбор данных (парсинг) из комментариев Twitch и/или YouTube для подачи на вход модели.

## Продукт-менеджер
9. Провести проблемные интервью 10 ноябрь и 10 декабрь
10. Составление дорожной карты развития проекта
11. Финансовое моделирование (unit экономика)
12. Расшифровка проблемных интервью (кто ЦА, какие сегменты, уникальное коммерческое предложение)

## Frontend-разработчик
13. Создать лендинг с возможностью приобрести демо


# Метрики для оценки успеха проекта

* Точность анализа эмоций и токсичности.
Выбрать подходящую метрику для классификации эмоций и токсичных комментариев (точность, полнота, F1-score) 

* Скорость обработки комментариев в реальном времени.
Цель — минимизировать задержку для обработки и реакции на комментарии, чтобы обеспечить быстрый ответ аудитории.
* Количество замаскированной ненормативной лексики, которую система успешно распознает