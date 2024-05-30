package com.example.request_manager.model;

import jakarta.persistence.*;

@Entity
public class ProcesamientoSolicitud {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "solicitud_id", nullable = false)
    private Solicitud solicitud;

    @Column(nullable = false)
    private boolean aprobacion;

    @Column(columnDefinition = "TEXT")
    private String notasProcesamiento;

    // Getters y setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Solicitud getSolicitud() {
        return solicitud;
    }

    public void setSolicitud(Solicitud solicitud) {
        this.solicitud = solicitud;
    }

    public boolean isAprobacion() {
        return aprobacion;
    }

    public void setAprobacion(boolean aprobacion) {
        this.aprobacion = aprobacion;
    }

    public String getNotasProcesamiento() {
        return notasProcesamiento;
    }

    public void setNotasProcesamiento(String notasProcesamiento) {
        this.notasProcesamiento = notasProcesamiento;
    }

    @Override
    public String toString() {
        return "ProcesamientoSolicitud{id=" + id + ", aprobacion=" + aprobacion + ", notasProcesamiento='"
                + notasProcesamiento + "'}";
    }
}
