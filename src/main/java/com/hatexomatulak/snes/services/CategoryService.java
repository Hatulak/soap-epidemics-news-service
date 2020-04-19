package com.hatexomatulak.snes.services;

import com.hatexomatulak.snes.models.CategoryDTO;
import com.hatexomatulak.snes.repositories.CategoryRepository;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Slf4j
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
@Service
public class CategoryService {
    @NonNull
    CategoryRepository categoryRepository;

    public List<CategoryDTO> findAll() {
        return categoryRepository.findAll();
    }

    public Optional<CategoryDTO> findById(Long id) {
        return categoryRepository.findById(id);
    }


    public CategoryDTO save(CategoryDTO experiment) {
        return categoryRepository.save(experiment);
    }

    public CategoryDTO update(CategoryDTO experiment) {
        return categoryRepository.save(experiment);
    }

    public void delete(CategoryDTO experiment) {
        categoryRepository.delete(experiment);
    }
}
