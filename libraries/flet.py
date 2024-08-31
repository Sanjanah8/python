import flet as ft

def main(page: ft.Page):
    page.add(ft.TextField(label="Enter your name:"))

ft.app(target=main)
