package com.example.request_manager.repository;

import com.example.request_manager.model.ProcesamientoSolicitud;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProcesamientoSolicitudRepository extends JpaRepository<ProcesamientoSolicitud, Long> {

}
