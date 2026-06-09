# Application

GitHub Actions пайплайны и Python Flask-приложение с экспортом метрик в Prometheus. Автоматическая сборка и публикация Docker-образа. Обновление Kubernetes Deployment при создании тега.

## Архитектура

> Flask-приложение подразумевает готовность [bootstrap](https://github.com/andrew-dibov/devops-bootstrap), [network](https://github.com/andrew-dibov/devops-network) и [kubernetes](https://github.com/andrew-dibov/devops-kubernetes)

### Слой 1 : Flask-приложение : Python Flask + Prometheus Exporter

| Функция | Описание |
| :-- | :-- |
| **Веб-приложение** | HTML-страница с сообщением из переменной окружения и `hostname` контейнера |
| **Параметризация** | Использование переменных окружения `MESSAGE`, `HOST` и `PORT` для конфигурации приложения |
| **Observability** | Экспорт метрик приложения по эндпоинту `/metrics` |

### Слой 2 : Контейнеризация : Docker

Dockerfile описывает получение базового образа, установку зависимостей, копирование исходного кода и определение команды запуска приложения.

### Слой 3 : CI/CD : GitHub Actions

| Пайплайн | Триггер | Действия |
| :-- | :-- | :-- |
| `build-push` | Push в ветку `main` или выполнение `workflow_dispatch` | Сборка Docker-образа -> публикация в реестре контейнеров |
| `build-push-release` | Push тега | Выполнение `build-push` -> обновление Kubernetes Deployment |

### Слой 4 : Конфигурация репозитория : Bash

Bash-скрипт выполняет обновление секретов и запускает `build-push` :

| Ключ | Значение |
| :-- | :-- |
| `CONFIG` | Содержимое `kubeconfig` |
| `REG_ID` | Идентификатор реестра контейнеров |
| `SA_KEY` | Ключ сервисного аккаунта |

## Технологии и навыки

| Категория | Технологии/Инструменты | Навыки |
| :-- | :-- | :-- |
| **CI/CD** | GitHub Actions | Настройка пайплайнов и управление секретами |
| **Containerization** | Docker, Container Registry | Сборка образа, тегирование образа, оптимизация кеша |
| **Orchestration** | Kubernetes | Обновление Deployment |
| **Programming** | Python, Flask, Flask Exporter | Микросервис с экспортом метрик и параметрами конфигурации |
| **Security** | GitHub Secrets, Lockbox | Безопасное хранение и передача данных |
| **Automation** | Bash, CLI | Автоматическая конфигурация репозитория |

## Развертывание

```bash
# скопировать и перейти
git clone git@github.com:andrew-dibov/devops-application.git && cd devops-application

# запустить скрипт инициализации
sudo chmod +x bash/* && ./bash/init.sh
```
