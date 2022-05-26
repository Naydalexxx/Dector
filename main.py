from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout


from kivymd.uix.picker import MDDatePicker
import datetime
import calendar

from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock

from kivymd.uix.picker import MDDatePicker


KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex
# Menu item in the DrawerList list.
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "150dp", "150dp"
            source: "data/logo/imag.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "naydalexxx@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



MDScreen: 

    MDNavigationLayout:
        

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"  
                        elevation: 10
                        md_bg_color: get_color_from_hex("#e7e4c0")
                        specific_text_color: get_color_from_hex("#4a4939")
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items:[["star-outline", lambda x: app.on_star_click()]]
                        
        
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        background_color:"#e7e4c0"
                        underline_color:"#4a4939"
                        text_color_normal:"#4a4939"
                        text_color_active:"blue"
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Input"
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"   
                                
                                BoxLayout:
                                    orientation: 'horizontal'                               
                                    
                                    MDIconButton:
                                        icon: "calendar-month"
                                        
                                    MDTextField:
                                        id: start_date
                                        hint_text: "Start date"
                                        on_focus: if self.focus: app.date_dialog()
                                
                                BoxLayout:
                                    orientation: 'horizontal'                         
                                    
                                    MDIconButton:
                                        icon: "cash"
                                        
                                    MDTextField:
                                        id: loan
                                        hint_text: "Loan"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'                                
                                    
                                    MDIconButton:
                                        icon: "clock-time-five-outline"
                                            
                                    MDTextField:
                                        id: months
                                        hint_text: "Months"
                                    
                                BoxLayout:
                                    orientation: 'horizontal'  
                                                       
                                    
                                    MDIconButton:
                                        icon: "bank"
                                            
                                    MDTextField:
                                        id: interest
                                        hint_text: "Interest, %"
                                    
                                    MDTextField:
                                        id: payment_type
                                        hint_text: "Payment type"
                                        on_focus: if self.focus: app.menu.open()
                                    MDSeparator:
                                        height: "1dp"
                                    BoxLayout:
                                        orientation: 'horizontal'
                                        AnchorLayout:
                                            anchor_x: 'center'
                                            MDIconButton:
                                                icon: "android"
                                                text: "BUTTON1"
                                                theme_text_color: "Custom"
                                                text_color: 1, 1, 1, 1
                                                line_color: 0, 0, 0, 1
                                                icon_color: 1, 0, 0, 1
                                                md_bg_color: 0.1, 0.1, 0.1, 1
                                                adaptive_width: True
                                                on_release: app.calc_table(*args)
                                        AnchorLayout:
                                            anchor_x: 'center'
                                            MDIconButton:
                                                icon: "android"
                                                text: "BUTTON2"
                                                theme_text_color: "Custom"
                                                text_color: 1, 1, 1, 1
                                                line_color: 0, 0, 0, 1
                                                icon_color: 1, 0, 0, 1
                                                md_bg_color: 0.1, 0.1, 0.1, 1
                                        AnchorLayout:
                                            anchor_x: 'center'
                                        
                                            Button:
                                                text: "Test Ok"
                                                size_hint_y: .5
                                                background_color: (0.1, 0.1, 0.1, 1.0)
                                                
                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Table"
                        Tab:
                            id: tab3
                            name: 'tab3'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] Graph"
                        
                        Tab:
                            id: tab4
                            name: 'tab4'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Chart"
                        
                        Tab:
                            id: tab5
                            name: 'tab5'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Sum"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
                

'''



class Tab(MDFloatLayout, MDTabsBase):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class MorgageCalkulatorApp(MDApp):
    title = "Moetgage Colkulator"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_for_calc_is_changed = True

        self.screen = Builder.load_string(KV)
        # https://kivymd.readthedocs.io/en/latest/components/menu/?highlight=MDDropDownItem#center-position
        # menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        menu_items = [{"icon": "format-text-rotation-angle-up", "text": "annuity"},
                      {"icon": "format-text-rotation-angle-down", "text": "differentiated"}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4,
        )
        self.menu.bind(on_release=self.set_item)

    def date_dialog(self):
        date_dialog = MDDatePicker(callback=self.get_date)


    def set_item(self, instance_menu, instance_menu_item):
        def set_item(interval):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()

        Clock.schedule_once(set_item, 0.5)



    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        print(date)
        self.screen.ids.start_date.text = date.strftime("%m/%d/%Y %H.%M.%S.%f")  # str(date)

    def build(self):
        self.icon = 'data/logo/KR.png'
        return self.screen

    def on_tab_switch(self, *args):
        # def on_tab_switch(self, instance_tabs, instance_tab, instance_tabs_label, tab_text):
        '''Called when switching tabs.
                :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
                :param instance_tab: <__main__.Tab object>;
                :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
                :param tab_text: text or name icon of tab;
                '''
        # print(instance_tab.name + " : " + tab_text)
        # print(args)
        # print("tab clicked!" + instance_tab.ids.label.text)
        ############# instance_tab.ids.label.text = tab_text
        # print(instance_tab.ids.label.text)
        if self.data_for_calc_is_changed:
            self.calc_table(self, args)
            self.data_for_calc_is_changed = False
        pass
    def on_start(self):
        icons_item = {
            "calculator-variant": "Input",
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",
            "book-open-variant": "Sum",

        }
        icons_it = {
            "gmail": "Gmail",
            "instagram": "instagram",
            "youtube": "Youtube",
            "twitter": "Twitter",
            "wikipedia": "Wikipedia",
        }

        for icon_name in icons_it.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_it[icon_name])
            )
        #for icon_name, name_tab in icons_item.items():
        #    self.root.ids.tabs.add_widget(Tab(text=f" [ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref] {name_tab}"))

    def calc_table(self, *args):
        print("button1 pressed")
        start_date = self.screen.ids.start_date.text
        loan = self.screen.ids.loan.text
        months = self.screen.ids.months.text
        interest = self.screen.ids.interest.text
        payment_type = self.screen.ids.payment_type.text
        print(start_date + "/" + loan + "/" + months + "/" + interest + "/" + payment_type)
        # convert to date object, float, and so on
        start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, '%m/%d/%Y %H/%M/%S/%f').date()
        loan = float(loan)
        months = int(months)
        interest = float(interest)

        row_data_for_tab = []
        # annuity payment
        # https://temabiz.com/finterminy/ap-formula-i-raschet-annuitetnogo-platezha.html
        percent = interest / 100 / 12
        monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))
        # print(monthly_payment)

    def on_star_click(self):
        pass

MorgageCalkulatorApp().run()