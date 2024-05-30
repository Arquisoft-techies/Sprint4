package com.example.request_manager.service;

import com.example.request_manager.model.ProcesamientoSolicitud;
import com.example.request_manager.model.Solicitud;
import com.example.request_manager.repository.ProcesamientoSolicitudRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Random;

@Service
public class ProcessingLogicService {

    @Autowired
    private ProcesamientoSolicitudRepository procesamientoSolicitudRepository;

    public ProcesamientoSolicitud crearProcesamiento(Solicitud solicitud) {
        boolean aprobacion = new Random().nextBoolean();
        String notasProcesamiento;

        if (aprobacion) {
            notasProcesamiento = "Buen perfil financiero, responsable con sus gastos y pagos.";
        } else {
            notasProcesamiento = "Perfil poco confiable, grandes índices de riesgos.";
        }

        ProcesamientoSolicitud procesamiento = new ProcesamientoSolicitud();
        procesamiento.setSolicitud(solicitud);
        procesamiento.setAprobacion(aprobacion);
        procesamiento.setNotasProcesamiento(notasProcesamiento);

        return procesamientoSolicitudRepository.save(procesamiento);
    }
}
