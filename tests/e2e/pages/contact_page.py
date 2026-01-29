from .base_page import BasePage


class ContactPage(BasePage):
    def open(self):
        self.page.goto("https://automationexercise.com/contact_us")

    def submit_form(self, name, email, subject, message):
        self.fill("input[name='name']", name)
        self.fill("input[name='email']", email)
        self.fill("input[name='subject']", subject)
        self.fill("textarea[name='message']", message)
        self.click("input[name='submit']")

    def success_visible(self):
        return self.is_visible("text=Success! Your details have been submitted successfully.")
