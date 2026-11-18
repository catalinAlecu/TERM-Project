"""Entry point for the TERM mobile application."""

import flet as ft


def main(page: ft.Page) -> None:
    """Build the initial mobile application screen."""
    page.title = "TERM"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = "#F7F9FC"

    def show_placeholder(event: ft.ControlEvent) -> None:
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"{event.control.label} is ready for the next feature.")
        )
        page.snack_bar.open = True
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("TERM", weight=ft.FontWeight.BOLD),
        center_title=False,
        bgcolor="#FFFFFF",
        elevation=1,
    )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Welcome to TERM",
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    "Your mobile app starts here.",
                                    size=16,
                                    color="#5F6B7A",
                                ),
                            ],
                            spacing=8,
                        ),
                        padding=ft.padding.only(left=20, right=20, top=24, bottom=16),
                    ),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Icon(
                                        ft.Icons.ROCKET_LAUNCH_OUTLINED,
                                        size=40,
                                        color="#2563EB",
                                    ),
                                    ft.Text(
                                        "Ready to build",
                                        size=20,
                                        weight=ft.FontWeight.W_600,
                                    ),
                                    ft.Text(
                                        "Replace this starter content with your first feature.",
                                        color="#5F6B7A",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=10,
                            ),
                            padding=24,
                        ),
                        margin=ft.margin.symmetric(horizontal=16),
                    ),
                    ft.Container(expand=True),
                ],
                expand=True,
            ),
            expand=True,
        )
    )

    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Home",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
                label="Settings",
            ),
        ],
        on_change=show_placeholder,
    )


if __name__ == "__main__":
    ft.run(main)
