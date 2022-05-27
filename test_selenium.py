import time
import pytest
from SeleniumTest import SeleniumTest

url = "http://www5.trf5.jus.br/cp/"
selenium_class = SeleniumTest(url)

# Testa se o usuário não foi redirecionado
def test_url():
    assert selenium_class.getUrl() == url

# Testa se a response não veio vazia
def test_response():
    assert selenium_class.getPage() != None

# Testa se a opção de numero foi clicada
def test_click():
    selenium_class.moveToElement("//label[contains(.,'Nº do processo')]")
    element = selenium_class.getElementByXPath("//label[contains(.,'Nº do processo')]")
    element.click()
    input_check = selenium_class.getElementByXPath("//label[contains(.,'Nº do processo')]/following-sibling::input")
    assert input_check.get_attribute("checked") == "true"

# Testa se a consulta foi realizada com sucesso
def test_consulta():
    selenium_class.sendKeys("//input[@id='filtro']", "0015648-78.1999.4.05.0000")
    element = selenium_class.getElementByID("submitConsulta")
    element.submit()
    selenium_class.changeToNextWindow()
    time.sleep(5) # espera por 5 segundos
    assert "PROCESSO Nº 0015648-78.1999.4.05.0000" in selenium_class.getPage()

# Finaliza os testes
def test_end():
    selenium_class.closeDriver()
