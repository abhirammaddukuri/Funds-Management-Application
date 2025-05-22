from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast

class FundManager:
    def __init__(self):
        self.depositors = {}

    def add_depositor(self, name, amount):
        self.depositors[name] = self.depositors.get(name, 0) + amount
        return f"{name} added: ₹{amount}. Total: ₹{self.depositors[name]}"

    def spend_money(self, amount, selected_depositors=None):
        if selected_depositors:
            selected_depositors = [name.strip() for name in selected_depositors.split(",") if name.strip() in self.depositors]
        else:
            selected_depositors = list(self.depositors.keys())
        
        if not selected_depositors:
            return "No valid depositors selected."
        
        split_amount = amount / len(selected_depositors)
        for name in selected_depositors:
            self.depositors[name] -= split_amount
        return f"Spent ₹{amount}. Each selected depositor deducted ₹{split_amount:.2f}."

    def show_balances(self):
        if not self.depositors:
            return "No depositors available."
        balances = "Balances:\n"
        for name, balance in self.depositors.items():
            balances += f"{name}: ₹{balance:.2f}\n"
        balances += f"Total Funds: ₹{sum(self.depositors.values()):.2f}"
        return balances

class FundApp(MDApp):
    def build(self):
        self.manager = FundManager()
        self.theme_cls.primary_palette = "Blue"
        
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.output_label = MDLabel(text="Welcome to Funds Manager", theme_text_color="Primary")
        layout.add_widget(self.output_label)
        
        self.name_input = MDTextField(hint_text='Depositor Name')
        self.amount_input = MDTextField(hint_text='Amount', input_filter='float')
        layout.add_widget(self.name_input)
        layout.add_widget(self.amount_input)
        
        add_button = MDRaisedButton(text="Add Depositor", on_release=self.add_depositor)
        layout.add_widget(add_button)
        
        self.spend_input = MDTextField(hint_text='Amount to Spend', input_filter='float')
        self.selected_input = MDTextField(hint_text='Enter depositors (comma-separated)')
        layout.add_widget(self.spend_input)
        layout.add_widget(self.selected_input)
        
        spend_button = MDRaisedButton(text="Spend Money", on_release=self.spend_money)
        layout.add_widget(spend_button)
        
        show_balance_button = MDRaisedButton(text="Show Balances", on_release=self.show_balances)
        layout.add_widget(show_balance_button)
        
        return layout
    
    def add_depositor(self, instance):
        name = self.name_input.text
        amount = self.amount_input.text
        if name and amount:
            message = self.manager.add_depositor(name, float(amount))
            toast(message)
    
    def spend_money(self, instance):
        amount = self.spend_input.text
        selected = self.selected_input.text
        if amount:
            message = self.manager.spend_money(float(amount), selected)
            toast(message)
    
    def show_balances(self, instance):
        message = self.manager.show_balances()
        dialog = MDDialog(title="Balances", text=message)
        dialog.open()

if __name__ == "__main__":
    FundApp().run()
