package com.example.request_manager.repository;

import com.example.request_manager.model.RegistroSolicitud;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RegistroSolicitudRepositorio extends JpaRepository<RegistroSolicitud, Long> {

}
