# Приложение

Пайплайны и Flask-приложение с экспортом метрик в Prometheus. Автоматическая сборка и публикация образа через GitHub Actions. Обновление Deployment в Kubernetes при создании тега.

## Архитектура

> Проект опирается на [kubernetes](https://github.com/andrew-dibov/devops-kubernetes)

### Слой 1 : Приложение : Flask + Prometheus

| Функция | Описание |
| :-- | :-- |
| **Веб-приложение** | HTML с сообщением и именем контейнера |
| **Observability** | Экспорт метрик по эндпоинту `/metrics` |
| **Параметризация** | Переменные окружения : `MESSAGE`, `HOST` и `PORT` |

### Слой 2 : Контейнеризация : Docker

Получение исходного образа, установка зависимостей через `requirements.txt`, копирование исходников и определение команды запуска приложения.

### Слой 3 : CI/CD : GitHub Actions

| Workflow | Триггер | Действия |
| :-- | :-- | :-- |
| `build-push` | Push в `main` или через `workflow_dispatch` | Сборка образа -> публикация в реестре |
| `build-push-release` | Push `tag` | `build-push` + обновление Deployment |

### Слой 4 : Автоматизация конфигурации : Bash

Обновление секретов и первый запуск `build-push` :

| Ключ | Значение |
| :-- | :-- |
| `CONFIG` | Содержимое `kubeconfig` |
| `REG_ID` | Идентификатор реестра контейнеров |
| `SA_KEY` | Ключ сервисного аккаунта |

## Технологии и навыки

| Категория | Технологии/Инструменты | Навыки |
| :-- | :-- | :-- |
| **CI/CD** | GitHub Actions | Настройка пайплайнов, управление секретами |
| **Containerization** | Docker, Container Registry | Сборка образа, тегирование, оптимизация кеша |
| **Orchestration** | Kubernetes | Обновление Deployment |
| **Programming** | Python, Flask, Flask Exporter | Микросервис с метриками и параметрами конфигурации |
| **Security** | GitHub Secrets, Lockbox | Безопасное хранение и передача данных |
| **Automation** | Bash, CLI | Автоматическая конфигурация репозитория |

## Развертывание

```bash
# скопировать и перейти
git clone git@github.com:andrew-dibov/devops-application.git && cd devops-application

# запустить скрипт инициализации
sudo chmod +x bash/* && ./bash/init.sh
```
