package main.java.manejador_solicitudes.solicitudes;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/offers")

public class controller {
    @Autowired
    private ProductsHandlerService productsHandlerService;

    @Autowired
    private ServicesHandlerService servicesHandlerService;

    @PostMapping
    public ResponseEntity<?> offersView(@RequestBody Map<String, Object> requestData) {
        String requestType = determineRequestType(requestData);
        if (requestType == null) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(Map.of("error", "Tipo de solicitud no válido"));
        }

        Map<String, Object> response;
        if ("producto".equals(requestType)) {
            response = productsHandlerService.handleRequest(requestData);
        } else if ("servicio".equals(requestType)) {
            response = servicesHandlerService.handleRequest(requestData);
        } else {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(Map.of("error", "Tipo de solicitud no válido"));
        }

        return ResponseEntity.ok(response);
    }

    private String determineRequestType(Map<String, Object> requestData) {
        return (String) requestData.get("tipo");
    }
}
