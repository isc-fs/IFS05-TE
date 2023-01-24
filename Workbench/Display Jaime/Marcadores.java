public class Marcadores{  
    int id;
    double valor;

    public int getId(){  //atributos get
        return id;
    }
    public double getValor(){ 
        return valor;
    } 

    public void setId(int id){ //atributos set
        this.id=id;
    }
    public void setValor(double valor){ 
        this.valor=valor;
    }
    double velocidad;
    double acelerador;
    double freno;
    double t_motor;
    double t_inversor;
    double t_baterias;

    public double getVelocidad(){ //atributos get
        return velocidad;
    }
    public double getAcelerador(){ 
        return acelerador;
    }
    public double getFreno(){ 
        return freno;
    }
    public double getT_Motor(){ 
        return t_motor;
    }
    public double getT_Inversor(){ 
        return t_inversor;
    }
    public double getT_Baterias(){ 
        return t_baterias;
    }

    public void setVelocidad(double velocidad){ //atributos set
        this.velocidad=velocidad;
    }
     public void setAcelerador(double acelerador){ 
        this.acelerador=acelerador;
    }
    public void setFreno(double freno){ 
        this.freno=freno;
    }
    public void setT_Motor(double t_motor){ 
        this.t_motor=t_motor;
    }
    public void setT_Inversoe(double t_inversor){ 
        this.t_inversor=t_inversor;
    }
    public void setVelocidad(int velocidad){ 
        this.velocidad=velocidad;
    }
    public void setT_Baterias(int t_baterias){ 
        this.t_baterias=t_baterias;
    }   
}
    class Temperaturas extends Marcadores{ //subclase para las tyre temps

        double t_fl; //front left
        double t_fr; //front right
        double t_rl; //rear left 
        double t_rr; //rear right

        public double getT_Fl(){ //atributos get
            return t_fl;
        }
        public double getT_Fr(){ 
            return t_fr;
        }
        public double getT_Rl(){ 
            return t_rl;
        }
        public double getT_Rr(){ 
            return t_rr;
        }

    public void setT_Fl(double t_fl){ //atributos set
        this.t_fl=t_fl;
    }
    public void setT_Fr(double t_fr){ 
        this.t_fr=t_fr;
    }
    public void setT_Rl(double t_Rl){ 
        this.t_rl=t_rl;
    }
    public void setT_Rr(double t_rr){ 
        this.t_rr=t_rr;
    }
}


