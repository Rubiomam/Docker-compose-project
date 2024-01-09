package main

import (
    "fmt"
    "database/sql"
    "html/template"
    "log"
    "net/http"

    _ "github.com/lib/pq"
)

func main() {
    // Conexión a la base de datos
    connStr := "user=arubio password=ccJan2024 dbname=biblioteca host=postgres port=5432 sslmode=disable"
    db, err := sql.Open("postgres", connStr)
    if err != nil {
        log.Fatal("Error al conectar a la base de datos.", err)
    }
    defer db.Close()

    // Servicio a archivos estáticos
    http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))

    // Configuración de plantillas
    templates := template.Must(template.ParseGlob("templates/*.html"))

    // Manejadores de rutas
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        err := templates.ExecuteTemplate(w, "index.html", nil)
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
        }
    })

    http.HandleFunc("/formulario", func(w http.ResponseWriter, r *http.Request) {
        if r.Method == http.MethodGet {
            err := templates.ExecuteTemplate(w, "formulario.html", nil)
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
            }
        } else if r.Method == http.MethodPost {
            err := r.ParseForm()
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }
            nombre := r.FormValue("nombre")
            
            // Insertar el nombre en la base de datos
            _, err = db.Exec("INSERT INTO usuarios (nombre) VALUES ($1)", nombre)
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                 return
            }    

            // Enviar respuesta al cliente
            fmt.Fprintf(w, "Hola, %s. ¡Bienvenido a la Biblioteca de Alejandría!", nombre)
        }

    })
  
    http.HandleFunc("/libro", func(w http.ResponseWriter, r *http.Request) {
        if r.Method == http.MethodGet {
            err := templates.ExecuteTemplate(w, "libro.html", nil)
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
            }
        } else if r.Method == http.MethodPost {
            err := r.ParseForm()
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }
            titulo := r.FormValue("titulo")
            autor := r.FormValue("autor")

            // Insertar el libro en la base de datos
            _, err = db.Exec("INSERT INTO libros (titulo, autor) VALUES ($1, $2)", titulo, autor)
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }

            // Enviar respuesta al cliente
            fmt.Fprintf(w, "Libro %s registrado con éxito.", titulo)
            }
        })
  
  http.HandleFunc("/prestamo", func(w http.ResponseWriter, r *http.Request) {
        if r.Method == http.MethodGet {
            err := templates.ExecuteTemplate(w, "prestamo.html", nil)
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
            }
      } else if r.Method == http.MethodPost {
            err := r.ParseForm()
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }
            usuarioID := r.FormValue("usuario_id")
            libroID := r.FormValue("libro_id")
            fechaPrestamo := r.FormValue("fecha_prestamo")

            // Registrar el préstamo en la base de datos
            _, err = db.Exec("INSERT INTO prestamos (usuario_id, libro_id, fecha_prestamo) VALUES ($1, $2, $3)", usuarioID, libroID, fechaPrestamo)
            if err != nil {
                http.Error(w, err.Error(), http.StatusInternalServerError)
                return
            }

            // Enviar respuesta al cliente
            fmt.Fprintf(w, "Préstamo registrado con éxito.")
            }
        })
        

    // Iniciar servidor
    log.Println("Iniciando servidor en http://localhost:8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

