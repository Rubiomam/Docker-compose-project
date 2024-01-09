package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	url := "http://servidor:8080/"

	resp, err := http.Get(url)
	if err != nil {
		log.Fatal("Error al realizar la solicitud: ", err)
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal("Error al leer la respuesta: ", err)
	}

	fmt.Println("Respuesta del servidor: ", string(body))
}