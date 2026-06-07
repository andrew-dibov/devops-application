# Приложение

Пайплайн под простое Flask-приложение с экспортом метрик в Prometheus. Автоматическая сборка и публикация образа через GitHub Actions. Обновление Deployment в Kubernetes при создании тега.

## Архитектура

> Проект опирается на [kubernetes](https://github.com/andrew-dibov/devops-kubernetes)

### Слой 1 : Приложение : Flask + Prometheus

| Функция | Описание |
| :-- | :-- |
| **Website** | `/` отображает сообщение из переменной окружения и имя контейнера |
| **Observability** | `/metrics` экспортирует метрики |
| **Конфигурация** | Переменные окружения : `MESSAGE`, `HOST`, `PORT` |

### Слой 2 : Контейнеризация : Docker

Получение начального образа, установка зависимостей, копирование исходникой и определение команды запуска.

### Слой 3 : CI/CD : GitHub Actions

| Workflow | Триггер | Действия |
| :-- | :-- | :-- |
| `build-push` | push в `main` или `workflow_dispatch` | Сборка образа -> публикация в реестре с тегами : `latest` и `github.sha` |
| `build-push-release` | push тега | `build-push` + обновление Deployment |

### Слой 4 : Автоматизация конфигурации : Bash

Обновление секретов и первый запуск `build-push` :

| Ключ | Значение |
| :-- | :-- |
| `CONFIG` | Содержимое `~/.kube/config` в base64 |
| `REG_ID` | Идентификатор реестра контейнеров |
| `SA_KEY` | Содержимое ключа сервисного аккаунта |

## Технологии и навыки

| Категория | Технологии/Инструменты | Навыки |
| :-- | :-- | :-- |
| **CI/CD** | GitHub Actions | Настройка пайплайнов, управление секретами, кеширование слоев |
| **Containerization** | Docker, Container Registry | Сборка образа, тегирование образа, оптимизация кеша |
| **Orchestration** | Kubernetes | Обновление образа в Deployment, проверка rollout |
| **Programming** | Python, Flask, Flask Exporter | Простой микросервис с метриками и параметрами |
| **Security** | GitHub Secrets, Lockbox | Безопасное хранение и передача данных |
| **Automation** | Bash, CLI | Автоматическая конфигурация репозитория |

## Развертывание

```bash
sudo chmod +x bash/* && ./bash/init.sh
```
