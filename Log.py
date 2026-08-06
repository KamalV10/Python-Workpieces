import logging as l

l.basicConfig(
    level=l.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

l.debug("Отладочная информация")
l.info("Приложение запущено")
l.warning("Внимание: низкий уровень диска")
l.error("Не удалось подключиться к БД")
l.critical("Критическая ошибка: остановка работы")