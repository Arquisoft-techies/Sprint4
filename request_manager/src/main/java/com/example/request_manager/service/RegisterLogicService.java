package com.example.request_manager.service;

import com.example.request_manager.model.ProcesamientoSolicitud;
import com.example.request_manager.model.RegistroSolicitud;
import com.example.request_manager.repository.RegistroSolicitudRepositorio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class RegisterLogicService {
    @Autowired
    private RegistroSolicitudRepositorio registroSolicitudRepositorio;

    public String agregarProcesamientoARegistro(ProcesamientoSolicitud procesamiento) {
        RegistroSolicitud registro = new RegistroSolicitud();
        registro.getProcesamientoSolicitud().add(procesamiento);

        registroSolicitudRepositorio.save(registro);

        return procesamiento.isAprobacion() + "-" + procesamiento.getNotasProcesamiento();
    }
}