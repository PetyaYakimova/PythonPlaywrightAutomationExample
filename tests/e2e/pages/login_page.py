from .base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        self.page.goto("https://automationexercise.com/login")

    def login(self, email, password):
        self.fill("input[data-qa='login-email']", email)
        self.fill("input[data-qa='login-password']", password)
        self.click("button[data-qa='login-button']")

    def error_visible(self):
        return self.is_visible("text=Your email or password is incorrect!")

    def start_signup(self, data):
        self.fill("input[data-qa='signup-name']", data["name"])
        self.fill("input[data-qa='signup-email']", data["email"])
        self.click("button[data-qa='signup-button']")

    def complete_signup(self, data):
        # Title
        self.page.click("input#id_gender1")

        # Password
        self.fill("input[data-qa='password']", data["password"])

        # Date of Birth (static values for stability)
        self.page.select_option("#days", "1")
        self.page.select_option("#months", "1")
        self.page.select_option("#years", "2000")

        # Address Information
        self.fill("input[data-qa='first_name']", data["first_name"])
        self.fill("input[data-qa='last_name']", data["last_name"])
        self.fill("input[data-qa='address']", data["address"])

        self.page.select_option("select[data-qa='country']", data["country"])

        self.fill("input[data-qa='state']", data["state"])
        self.fill("input[data-qa='city']", data["city"])
        self.fill("input[data-qa='zipcode']", data["zipcode"])
        self.fill("input[data-qa='mobile_number']", data["mobile"])

        self.click("button[data-qa='create-account']")

    def success_message_visible(self):
        return self.is_visible("text=Account Created!")
