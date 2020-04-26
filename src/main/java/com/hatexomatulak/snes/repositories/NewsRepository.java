package com.hatexomatulak.snes.repositories;

import com.hatexomatulak.snes.models.NewsDTO;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface NewsRepository extends CrudRepository<NewsDTO, Integer> {
    List<NewsDTO> findAll();
}
