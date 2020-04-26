package com.hatexomatulak.snes.repositories;

import com.hatexomatulak.snes.models.CategoryDTO;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CategoryRepository extends CrudRepository<CategoryDTO, Integer> {
    List<CategoryDTO> findAll();
}
