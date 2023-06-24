from django.db import models

class Alert(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome")
    description = models.TextField(blank=True, null=True)

    formula = models.CharField(max_length=90, verbose_name="Fórmula")

    project = models.ForeignKey("core.Project", on_delete=models.CASCADE, verbose_name="Projeto")
    devices = models.ManyToManyField("core.Device", verbose_name="Dispositivos para os quais o alerta se aplica")

    risk = models.BooleanField(default=False, verbose_name="Risco")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Alerta"
        verbose_name_plural = "Alertas"


    def formula_validation(self):
        f = self.formula
        root_params = [x.model.id_tag for x in self.devices.all()]
        params = []

        for rp in root_params:
            params.extend(
                [
                    f"{rp}:temp_1h",
                    f"{rp}:temp_3h",
                    f"{rp}:temp_5h",
                    f"{rp}:temp_10h",
                    f"{rp}:temp_15h",
                    f"{rp}:temp_20h",
                    f"{rp}:temp_1d",
                    f"{rp}:temp_2d",
                    f"{rp}:temp_3d"
                ]
            )

        while "[" in f:
            try:
                i = f.index("[")
                j = f.index("]")
            except ValueError:
                return False

            param = f[i+1:j]
            if param not in params:
                return False

            f = f[j+1:]
        return True

    def verify(self):
        in_alert = self.verify_formula()
        print(in_alert)
        if in_alert:
            self.send_notification()
            self.risk = True
            self.save()

    def get_param_value(self, param):
        for device in self.devices:
            if device.model.id_tag == param:
                return device.get_last_value(param)

    def verify_formula(self):
        f = self.formula
        final = ""
        while "[" in f:
            i = f.index("[")
            j = f.index("]")

            param = f[i+1:j]
            value = self.get_param_value(param)

            final += f[:i] + str(value) + f[j+1:]
        else:
            final += f
        return eval(final)

    def send_notification(self):
        pass