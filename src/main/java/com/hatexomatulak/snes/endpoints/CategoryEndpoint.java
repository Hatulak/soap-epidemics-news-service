package com.hatexomatulak.snes.endpoints;

import com.hatexomatulak.snes.exception.DBException;
import com.hatexomatulak.snes.models.CategoryDTO;
import com.hatexomatulak.snes.models.NewsDTO;
import com.hatexomatulak.snes.services.CategoryService;
import com.project.xml.category.*;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import java.util.ArrayList;
import java.util.List;

@Slf4j
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
@Endpoint
public class CategoryEndpoint {
    private static final String NAMESPACE_URI = "http://www.project.com/xml/category";

    @NonNull
    private CategoryService categoryService;


    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "AuthorizeRequest")
    @ResponsePayload
    public AuthorizeResponse authorize(@RequestPayload AuthorizeRequest request) {
        AuthorizeResponse response = new AuthorizeResponse();
        if (request.getLogin().equals("admin") && request.getPassword().equals("admin"))
            response.setIsAuthorize(true);
        else
            response.setIsAuthorize(false);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "CreateCategoryRequest")
    @ResponsePayload
    public CreateCategoryResponse createNews(@RequestPayload CreateCategoryRequest request) {
        CategoryDTO categoryDTO = new CategoryDTO(request.getName(), new ArrayList<NewsDTO>());
        CategoryDTO saved = categoryService.save(categoryDTO);
        CreateCategoryResponse response = new CreateCategoryResponse();
        response.setCategory(saved.castToCategory());
        return response;
    }

    @SneakyThrows(DBException.class)
    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "GetCategoryByIdRequest")
    @ResponsePayload
    public CreateCategoryResponse getCategoryById(@RequestPayload GetCategoryByIdRequest request) {
        try {
            CategoryDTO categoryDTO = categoryService.findById(request.getId()).orElseThrow(DBException::new);
            CreateCategoryResponse response = new CreateCategoryResponse();
            response.setCategory(categoryDTO.castToCategory());
            return response;
        } catch (DBException e) {
            log.error("[getNewsById] Problem with database, cannot find category  by categoryId. Id:  " + request.getId());
            throw new DBException("Problem with database, cannot find category by categoryId");
        }
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "GetAllCategoryRequest")
    @ResponsePayload
    public GetAllCategoryResponse getAllCategory(@RequestPayload GetAllCategoryRequest request) {
        List<CategoryDTO> allCategories = categoryService.findAll();
        List<Category> result = new ArrayList<>();
        allCategories.forEach(p -> result.add(p.castToCategory()));
        GetAllCategoryResponse response = new GetAllCategoryResponse();
        response.getCategory().addAll(result);
        return response;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "UpdateCategoryRequest")
    @ResponsePayload
    public CreateCategoryResponse updateCategory(@RequestPayload UpdateCategoryRequest request) throws DBException {
        try {
            CategoryDTO categoryDTO = categoryService.findById(request.getId()).orElseThrow(DBException::new);
            categoryDTO.setName(request.getName());
            CategoryDTO saved = categoryService.save(categoryDTO);
            CreateCategoryResponse response = new CreateCategoryResponse();
            response.setCategory(saved.castToCategory());
            return response;
        } catch (DBException e) {
            log.error("[getNewsById] Problem with database, cannot find category  by categoryId. Id:  " + request.getId());
            throw new DBException("Problem with database, cannot find category by categoryId");
        }
    }

    @SneakyThrows(DBException.class)
    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "DeleteCategoryByIdRequest")
    @ResponsePayload
    public DeleteCategoryResponse deleteCategory(@RequestPayload DeleteCategoryByIdRequest request) {
        try {
            CategoryDTO categoryDTO = categoryService.findById(request.getId()).orElseThrow(DBException::new);
            categoryService.delete(categoryDTO);
            DeleteCategoryResponse response = new DeleteCategoryResponse();
            response.setResult("Success");
            return response;
        } catch (DBException e) {
            log.error("[getNewsById] Problem with database, cannot find category  by categoryId. Id:  " + request.getId());
            throw new DBException("Problem with database, cannot find category by categoryId");
        }
    }

}
