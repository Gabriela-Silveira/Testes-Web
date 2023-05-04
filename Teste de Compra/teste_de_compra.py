# Teste de compra
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Configura
nome = ''
sobrenome = ''
email = ''
telefone = ''
endereco1 = ''
endereco2 = ''
cidade = ''
pag_aprov = 'Thank you. Your order has been received.'
info_pag = 'Make your payment directly into our bank account. Please use your Order ID as the payment reference. Your ' \
           'order won’t be shipped until the funds have cleared in our account. '
valor_total = ''

# Executa
class Testes_de_compra:

    def setup_method(self):
        self.driver = webdriver.Chrome(
            'C:\\Users\\gabri\\PycharmProjects\\Testes_do_site_demo\\drivers\\chromedriver.exe')

    # Fim
    def teardown_method(self):
        self.driver.quit()

    # Meio
    def test_login_invalid(self):
        self.driver.get('http://practice.automationtesting.in/')  # abrir o site
        self.driver.find_element(By.ID, 'menu-item-40').click() # entrar na página de compras
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="woocommerce_product_categories-2"]/ul/li[3]').click() # filtrar por JavaScript
        self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[3]/a[2]').click() # adiciona o item ao carrinho
        assert self.driver.find_element(By.CSS_SELECTOR, ".cartcontents").text == "1 Item" # confere se o item aparece no carrinho
        self.driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents").click() # acessa o carrinho
        self.driver.find_element(By.CSS_SELECTOR, ".cart-subtotal > td").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".cart-subtotal > th").text == "Subtotal"
        self.driver.find_element(By.CSS_SELECTOR, ".tax-rate").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".tax-rate > th").text == "Tax"
        self.driver.find_element(By.CSS_SELECTOR, ".order-total").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".order-total > th").text == "Total"
        self.driver.find_element(By.CSS_SELECTOR, ".checkout-button").click() # clica no botão de finalizar compra
        self.driver.find_element(By.ID, "billing_first_name").click()
        self.driver.find_element(By.ID, "billing_first_name").send_keys({nome})
        self.driver.find_element(By.ID, "billing_last_name").send_keys({sobrenome})
        self.driver.find_element(By.ID, "billing_email").send_keys({email})
        self.driver.find_element(By.ID, "billing_phone").send_keys({telefone})
        self.driver.find_element(By.ID, "billing_country_field").click()
        element = self.driver.find_element(By.ID, "select2-chosen-1") # selecionar país
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.ID, "select2-chosen-1")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "select2-drop-mask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "billing_address_1").click()
        self.driver.find_element(By.ID, "billing_address_1").send_keys({endereco1})
        self.driver.find_element(By.ID, "billing_address_2").send_keys({endereco2})
        self.driver.find_element(By.ID, "billing_city").send_keys({cidade})
        element = self.driver.find_element(By.ID, "select2-chosen-2")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.ID, "select2-chosen-2")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "select2-drop-mask")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "payment_method_cheque").click() # metodo de pagamento
        element = self.driver.find_element(By.ID, "payment_method_cod")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".wc_payment_method:nth-child(1)").click()
        self.driver.find_element(By.ID, "payment_method_bacs").click()
        self.driver.find_element(By.ID, "place_order").click()
        element = self.driver.find_element(By.ID, "place_order")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".woocommerce-thankyou-order-received").click()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".woocommerce-thankyou-order-received").text == {pag_aprov}
        self.driver.find_element(By.ID, "body").click()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        "p:nth-child(4)").text == {info_pag}
        self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(7)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h2:nth-child(7)").text == "Order Details"
        self.driver.find_element(By.CSS_SELECTOR, "tfoot > tr:nth-child(1) > th").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shop_table").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) .woocommerce-Price-amount").text == {
            valor_total}
