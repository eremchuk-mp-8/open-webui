# Open WebUI 👋

## Установка и запуск

Предварительно загрузите репозиторий
```bash
git clone https://github.com/eremchuk-mp-8/open-webui.git
cd open-webui
 ```

Следуйте руководству [https://docs.openwebui.com/getting-started/advanced-topics/development] (Local Development Guide), начиная с пункта **3. Backend Setup**.

После выполнения всех шагов сервер бэкенда становится доступен по адресу [http://localhost:8080/docs] (http://localhost:8080/docs).

## Модификации
Добавлены модули, реализующие счётчик использования промптов.
```bash
\open-webui\backend\open_webui\models\promptusages.py
\open-webui\backend\open_webui\routers\promptusages.py
```
Функция increment увеличивает значение счётчика использований выбранного промпта.

Получение значения счётчика по выбранному промпту осуществляется по эндпоинту
```bash
 /api/v1/promptusages/{command}/usage
```

## License 📜

This project is licensed under the [Open WebUI License](LICENSE), a revised BSD-3-Clause license. You receive all the same rights as the classic BSD-3 license: you can use, modify, and distribute the software, including in proprietary and commercial products, with minimal restrictions. The only additional requirement is to preserve the "Open WebUI" branding, as detailed in the LICENSE file. For full terms, see the [LICENSE](LICENSE) document. 📄

Created by [Timothy Jaeryang Baek](https://github.com/tjbck) - Let's make Open WebUI even more amazing together! 💪