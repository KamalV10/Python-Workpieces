import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.debug("Отладочная информация")
logging.info("Приложение запущено")
logging.warning("Внимание: низкий уровень диска")
logging.error("Не удалось подключиться к БД")
logging.critical("Критическая ошибка: остановка работы")
