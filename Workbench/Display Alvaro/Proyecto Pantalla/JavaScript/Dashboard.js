class Dashboard {
    constructor(velocidad, potencia, SoC, FL_temp, FR_temp, RL_temp, RR_temp) {
        this.velocidad = velocidad;
        this.potencia = potencia;
        this.SoC = SoC;
        this.FL_temp = FL_temp;
        this.FR_temp = FR_temp;
        this.RL_temp = RL_temp;
        this.RR_temp = RR_temp;
    }

    updateVelocidad(valor) {
        this.velocidad = valor;
    }

    updatePotencia(valor) {
        this.potencia = valor;
    }

    updateSoC(valor) {
        this.SoC = valor;
    }

    updateFL_temp(valor) {
        this.FL_temp = valor;
    }

    updateFR_temp(valor) {
        this.FR_temp = valor;
    }

    updateRL_temp(valor) {
        this.RL_temp = valor;
    }

    updateRR_temp(valor) {
        this.RR_temp = valor;
    }

    display() {
        console.log("Velocidad: " + this.velocidad + " KM/H");
        console.log("Potencia: " + this.potencia + " KW");
        console.log("SoC: " + this.SoC + "%");
        console.log("Tyre temps: \n" + "\t " + FL_temp + "      " + FR_temp +
            "\n \t" + RL_temp + "      " + RR_temp);
    }

    periodicUpdate() {
        setInterval(() => {
            // Aquí se coloca el código para actualizar los valores de los atributos
            // Puede ser una llamada a una API, una lectura de un sensor, etc.
            this.updateVelocidad(this.velocidad + 1);
            this.updatePotencia(this.potencia + 2);
            this.updateSoC(this.SoC - 1);
            this.updateMarcha(this.marcha + 1);
        }, 10);
    }
}

let dashboard = new Dashboard(0, 0, 100, 0, 0, 0, 0);
dashboard.periodicUpdate();