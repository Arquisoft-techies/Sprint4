package com.example.request_manager.service;

import com.example.request_manager.model.Solicitud;
import com.example.request_manager.model.ProcesamientoSolicitud;
import com.example.request_manager.repository.SolicitudRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class RequestLogicService {
    @Autowired
    private SolicitudRepository solicitudRepository;

    @Autowired
    private ProcessingLogicService processingLogicService;

    @Autowired
    private RegisterLogicService registerLogicService;

    public String crearSolicitud(Long id, String tipo, boolean estado) {
        Solicitud solicitud = new Solicitud();
        solicitud.setId(id);
        solicitud.setTipo(tipo);
        solicitud.setEstado(estado);

        solicitudRepository.save(solicitud);

        return procesamientoSolicitud(solicitud);
    }

    private String procesamientoSolicitud(Solicitud solicitud) {
        ProcesamientoSolicitud procesamiento = processingLogicService.crearProcesamiento(solicitud);
        return registerLogicService.agregarProcesamientoARegistro(procesamiento);
    }
}
