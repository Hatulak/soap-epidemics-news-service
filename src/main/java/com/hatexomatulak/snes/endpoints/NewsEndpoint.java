package com.hatexomatulak.snes.endpoints;

import com.hatexomatulak.snes.models.NewsDTO;
import com.hatexomatulak.snes.services.NewsService;
import com.project.xml.news.GetNewsByIdRequest;
import com.project.xml.news.GetNewsResponse;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

@Slf4j
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
@Endpoint
public class NewsEndpoint {
    private static final String NAMESPACE_URI = "http://www.project.com/xml/news";

    @NonNull
    private NewsService newsService;

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "GetNewsByIdRequest")
    @ResponsePayload
    public GetNewsResponse getNewsById(@RequestPayload GetNewsByIdRequest request) throws Exception {

        NewsDTO newsDTO = newsService.findById(request.getId()).orElseThrow(Exception::new);
        GetNewsResponse response = new GetNewsResponse();

        response.setNews(newsDTO.castToNews());
        return response;

    }

}
