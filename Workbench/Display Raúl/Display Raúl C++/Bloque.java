//package main;

public class Bloque
{
	int x,y,length,height;
	
	public Bloque(int x, int y, int length, int height)
	{
		this.setX(x);
		this.setY(y);
		this.setLength(length);
		this.setHeight(height);
	}
	
	public void setX(int valor)
	{
		this.x = valor;
	}
	
	public void setY(int valor)
	{
		this.y = valor;
	}
	
	public void setLength(int valor)
	{
		this.length = valor;
	}
	
	public void setHeight(int valor)
	{
		this.height = valor;
	}
}