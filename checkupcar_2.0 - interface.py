from flet import *
import datetime

url = "https://tse1.mm.bing.net/th/id/OIG3.03apNkPdyjJDBAj.dtpg?pid=ImgGn"

def trocando(e):
    e.page.client_storage.set("selected_index", e.control.selected_index)
    if e.control.selected_index == 0:
        e.page.go("/carros")
    elif e.control.selected_index == 1:
        e.page.go("/adicionar_veiculo")
    elif e.control.selected_index == 2:
        e.page.go("/verificar_revisao")
    print(f"Aba selecionada: {e.control.selected_index}")

# Tabs definindo seu conteúdo corretamente
minhatab = Tabs(
    selected_index=0,
    animation_duration=300,
    unselected_label_color="black",
    label_color="white",
    indicator_color="white",
    indicator_border_radius=30,
    divider_color="#7c59f0",
    scrollable=True,
    on_change=trocando,
    tabs=[
        Tab(
            text="Carros",
            icon=icons.DIRECTIONS_CAR,
        ),
        Tab(
            text="Adicionar Veículo",
            icon=icons.CAR_RENTAL,
        ),
        Tab(
            text="Verificar Revisão",
            icon=icons.CAR_REPAIR,
        ),
    ]
)

def main(page: Page):
    selected_index = page.client_storage.get("selected_index", 0)
    minhatab.selected_index = selected_index
    page.title = "CheckUp Car"

    minha_barra = Container(
        border_radius=border_radius.vertical(bottom=30),
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color="#fc4795",
        ),
        gradient=LinearGradient(
            begin=alignment.top_left,
            end=alignment.bottom_right,
            colors=["#fc4795", "#7c59f0"]
        ),
        width=400,
        height=150,
        padding=10,
        content=Column([
            Row([
                IconButton(icon="menu", icon_size=20, icon_color="white"),
                Text("CheckUp Car", size=25, color="white", weight="bold"),
                Row([
                    IconButton(icons.NOTIFICATIONS_ACTIVE_OUTLINED, icon_size=20, icon_color="white"),
                    IconButton(icons.SEARCH, icon_size=20, icon_color="white"),
                ])
            ], alignment="spaceBetween"),
            minhatab
        ])
    )

    def carros_view():
        return View(
            "/carros",
            [
                minha_barra,
                Container(
                    margin=margin.only(top=160),
                    alignment=alignment.center,
                    content=Column([
                        Text("Bem Vindo 😊", size=30),
                        Image(
                            url,
                            width=300,
                            height=300,
                        )
                    ])
                ),
            ]
        )

    def adicionar_veiculo_view():
        def salvar_click(e):
            marca = marca_field.value
            modelo = modelo_field.value
            quilometragem = quilometragem_field.value
            if not marca or not modelo or not quilometragem:
                page.snack_bar = SnackBar(Text("Todos os campos são obrigatórios!"))
                page.snack_bar.open = True
                page.update()
                return
            try:
                quilometragem = int(quilometragem)
            except ValueError:
                page.snack_bar = SnackBar(Text("Quilometragem deve ser um número!"))
                page.snack_bar.open = True
                page.update()
                return
            page.snack_bar = SnackBar(Text("Veículo salvo com sucesso!"))
            page.snack_bar.open = True
            page.update()
        
        marca_field = TextField(label="Marca do Carro", helper_text="Volkswagen, Toyota, BMW...")
        modelo_field = TextField(label="Modelo", helper_text="Jetta, Civic, A45...")
        quilometragem_field = TextField(label="Quilometragem")

        return View(
            "/adicionar_veiculo",
            [
                minha_barra,
                Container(
                    margin=margin.only(top=160),
                    alignment=alignment.center,
                    content=Column([
                        Text("Adicionar Veículo", size=30),
                        marca_field,
                        modelo_field,
                        quilometragem_field,
                        ElevatedButton(text="Salvar", on_click=salvar_click)
                    ])
                ),
            ]
        )

    def verificar_revisao_view():
        return View(
            "/verificar_revisao",
            [
                minha_barra,
                Container(
                    margin=margin.only(top=160),
                    alignment=alignment.center,
                    content=Column([
                        Text("Verificar Revisão", size=30),
                        TextField(label="Placa do Veículo", helper_text="Digite a placa para verificar revisões"),
                        ElevatedButton(text="Buscar", on_click=lambda e: page.snack_bar(Text("Busca realizada!")).open())
                    ])
                ),
            ]
        )

    def route_change(e):
        page.views.clear()
        page.views.append(carros_view())
        if page.route == "/adicionar_veiculo":
            page.views.append(adicionar_veiculo_view())
        elif page.route == "/verificar_revisao":
            page.views.append(verificar_revisao_view())
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    if page.route == "":
        page.go("/carros")
    else:
        page.go(page.route)

app(target=main)

