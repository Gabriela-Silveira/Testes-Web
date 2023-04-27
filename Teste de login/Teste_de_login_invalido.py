# Teste de login
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configura
email = 'gabriela.gsilveira@hotmail.com'
senha = '1234'

# Executa
# Inicio
class Testes:

    def setup_method(self):
        self.driver = webdriver.Chrome(
            'C:\\Users\\gabri\\PycharmProjects\\Testes_do_site_demo\\drivers\\chromedriver.exe')

    # Fim
    def teardown_method(self):  # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    def test_login_invalid(self):
        self.driver.get('http://practice.automationtesting.in/')  # abrir o site
        self.driver.find_element(By.ID, 'menu-item-50').click() # acessar minha conta
        time.sleep(5)
        self.driver.find_element(By.ID, 'username').click()
        self.driver.find_element(By.ID, 'username').send_keys(f'{email}') # digitar e-mail
        self.driver.find_element(By.ID, 'password').click()
        self.driver.find_element(By.ID, 'password').send_keys(f'{senha}') # digitar senha
        self.driver.find_element(By.ID, 'rememberme').click() # ativar o lembre de mim
        self.driver.find_element(By.NAME, 'login').click()

        assert self.driver.find_element(By.CSS_SELECTOR, ".woocommerce-error > li").text == "Error: the password you entered for the username " \
                                           "gabriela.gsilveira@hotmail.com is incorrect. Lost your password?"

    # Valida

