import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        anni = self._model.getAnni()
        for a in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(data=a[0],text=f"{a[0]} - {a[1]}",on_click=self.readAnno))
        self._view.update_page()

    def readAnno(self,e):
        if e.control.data == None:
            self._view.txt_result.controls.append(ft.Text("seleziona un anno"))
        else:
            self.anno_scelto = e.control.data

    def handle_graph(self, e):
        self._model.buildGraph(self.anno_scelto)
        nodes = self._model.getNodes()
        for n in nodes:
            self._view.ddstates.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def analizza(self, e):
        if self._view.ddstates.value == None:
            self._view.txt_result.controls.append(ft.Text("Seleziona uno stato"))
            self._view.update_page()
            return
        pred ,succ = self._model.getps(self._view.ddstates.value)
        self._view.txt_result.controls.append(ft.Text(f"I predecessori sono {pred}"))
        self._view.txt_result.controls.append(ft.Text(f"I successori sono {succ}"))
        self._view.update_page()
        nodi_raggiungibili = self._model.getRaggiungibili(self._view.ddstates.value)
        self._view.txt_result.controls.append(ft.Text(f"I nodi raggiungibili da {self._view.ddstates.value} sono: {nodi_raggiungibili}"))
        self._view.update_page()


    def handle_path(self,e):
        path=self._model.getCammino(self._view.ddstates.value)
        self._view.txtOut2.controls.append(ft.Text(f"Il cammino migliore partendo da {self._view.ddstates.value} è: {path}"))
        self._view.update_page()
