from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def fill_field(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(value)

    def click_on_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_for_invisibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def click_java_script(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        raw_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", raw_element)

    def find_element_with_wait_for_change_element(self, locator, old_value):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)  #сначала ждем прогрузку элемента
        )
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(locator, old_value)   #потом ждем его изменение
        )
        return self.driver.find_element(*locator)

    def drag_and_drop(self, source_locator, target_locator):
        """
        Перетаскивает элемент из source_locator в target_locator с использованием JavaScript.
        :param source_locator: Локатор элемента, который нужно перетащить.
        :param target_locator: Локатор элемента, куда нужно перетащить.
        """
        self.find_element_with_wait(source_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)
