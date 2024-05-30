package com.example.request_manager.model;

import jakarta.persistence.*;
import java.util.Set;

@Entity
public class RegistroSolicitud {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToMany
    @JoinTable(name = "registro_procesamiento", joinColumns = @JoinColumn(name = "registro_solicitud_id"), inverseJoinColumns = @JoinColumn(name = "procesamiento_solicitud_id"))
    private Set<ProcesamientoSolicitud> procesamientoSolicitud;

    // Getters y setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Set<ProcesamientoSolicitud> getProcesamientoSolicitud() {
        return procesamientoSolicitud;
    }

    public void setProcesamientoSolicitud(Set<ProcesamientoSolicitud> procesamientoSolicitud) {
        this.procesamientoSolicitud = procesamientoSolicitud;
    }

    @Override
    public String toString() {
        return "RegistroSolicitud{id=" + id + "}";
    }
}
